"""Recompute what study_easier should output for the test cases, and check a run's output.

python3 tests/verify.py                      print the expected numbers for every case
python3 tests/verify.py CASE RUN.md          check a saved run against the expected numbers
python3 tests/verify.py --ics RUN.md         check the .ics block inside a saved run
"""
import math
import re
import sys
from datetime import date
from fractions import Fraction as F

# (course, item, due date, weight %, credits, hours, protected)
CASES = {
    "busy-week": {
        "today": date(2026, 11, 9),
        "weekly": 20,
        "items": [
            ("PSY 101", "Weekly quiz 4", date(2026, 11, 11), 2, 3, F(2), False),
            ("PSY 101", "Lab report", date(2026, 11, 13), 20, 3, F(10), False),
            ("STAT 120", "Problem set 5", date(2026, 11, 12), 5, 3, F(4), False),
            ("STAT 120", "Final exam", date(2026, 11, 30), 40, 3, F(15), False),
            ("HIST 210", "Essay", date(2026, 11, 20), 25, 4, F(10), False),
            ("HIST 210", "Seminar attendance log", date(2026, 11, 12), 5, 4, F(1, 2), True),
            ("DES 130", "Reading response", date(2026, 11, 10), 3, 3, F(2), False),
            ("DES 130", "Academic integrity declaration", date(2026, 11, 11), 0, 3, F(1, 2), True),
        ],
        # course: ([(weight, mark), ...finished items], target)
        "finals": {
            "PSY 101": ([(6, 90), (30, 58)], 90),
            "STAT 120": ([(35, 64), (20, 85)], 70),
        },
    },
    "exam-crunch": {
        "today": date(2026, 12, 3),
        "weekly": 45,
        "items": [
            ("CHEM 150", "Final exam", date(2026, 12, 7), 45, 3, F(20), False),
            ("BIO 140", "Lab practical", date(2026, 12, 8), 10, 3, F(3), True),
            ("BIO 140", "Poster", date(2026, 12, 10), 20, 3, F(7), False),
            ("PHIL 110", "Take-home essay", date(2026, 12, 7), 30, 3, F(10), False),
            ("PHIL 110", "Response paper 6", date(2026, 12, 4), 4, 3, F(2), False),
        ],
        "finals": {
            "CHEM 150": ([(55, 85)], 80),
            "BIO 140": ([(70, 88)], 60),
            "PHIL 110": ([(66, 72)], 75),
        },
    },
    "guided": {
        "today": date(2026, 11, 2),
        "weekly": 18,
        "items": [
            ("GEOG 105", "Field journal", date(2026, 11, 6), 15, 3, F(4), False),
            ("GEOG 105", "Field trip", date(2026, 11, 7), 5, 3, F(4), True),
            ("GEOG 105", "Map assignment", date(2026, 11, 11), 20, 3, F(6), False),
            ("GEOG 105", "Final exam", date(2026, 12, 3), 35, 3, F(15), False),
            ("PHYS 120", "Problem set 4", date(2026, 11, 9), 5, 4, F(3), False),
            ("PHYS 120", "Problem set 5", date(2026, 11, 16), 5, 4, F(3), False),
            ("PHYS 120", "Lab report 2", date(2026, 11, 13), 10, 4, F(6), False),
            ("PHYS 120", "Lab safety quiz", date(2026, 11, 3), 0, 4, F(1, 2), True),
            ("PHYS 120", "Final exam", date(2026, 12, 1), 30, 4, F(15), False),
        ],
        "finals": {
            "GEOG 105": ([(25, 72)], 75),
            "PHYS 120": ([(15, 90), (25, 81), (10, 78)], 85),
        },
    },
}


def urgency(days):
    if days <= 1:
        return F(3)
    if days <= 3:
        return F(2)
    if days <= 7:
        return F(3, 2)
    if days <= 14:
        return F(1)
    return F(1, 2)


def r1(x):
    """Round half up to 1 decimal, the way a person does it on paper."""
    return math.floor(float(x) * 10 + 0.5 + 1e-9) / 10


def plan(case):
    c = CASES[case]
    rows = []
    for course, item, due, weight, credits, hours, protected in c["items"]:
        days = (due - c["today"]).days
        stake = F(weight) * F(credits, 3)
        score = stake * urgency(days) / hours
        latest = days - math.ceil(hours * 7 / c["weekly"])
        rows.append(dict(course=course, item=item, due=due, days=days, stake=stake, hours=hours,
                         score=score, start_now=latest <= 0, protected=protected))
    rows.sort(key=lambda r: (-r["score"], r["due"]))
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    scores = sorted(r["score"] for r in rows)
    n = len(scores)
    median = scores[n // 2] if n % 2 else (scores[n // 2 - 1] + scores[n // 2]) / 2
    for r in rows:
        r["minimum"] = r["score"] < median and r["stake"] <= 5 and not r["protected"]
    # fit the week
    left = F(c["weekly"])
    order = sorted(rows, key=lambda r: (r["days"] > 7, not r["start_now"], r["rank"]))
    for r in order:
        r["this_week"] = min(r["hours"], left)
        left -= r["this_week"]
    finals = {}
    for course, (done, target) in c["finals"].items():
        earned = sum(F(w) * F(m, 100) for w, m in done)
        remaining = 100 - sum(w for w, _ in done)
        needed = (target - earned) / remaining * 100
        if needed <= 0:
            verdict = "already secured"
        elif needed > 100:
            verdict = f"not reachable · best reachable {r1(earned + remaining)}%"
        else:
            verdict = f"{r1(needed)}%"
        finals[course] = dict(earned=r1(earned), remaining=remaining, target=target,
                              needed=r1(needed), verdict=verdict)
    return rows, median, finals, F(c["weekly"]) - left


def show(case):
    rows, median, finals, planned = plan(case)
    print(f"== {case}  (planned {float(planned):g} h, median score {r1(median)})")
    for r in rows:
        tags = [t for t, on in (("START NOW", r["start_now"]), ("PROTECTED", r["protected"]),
                                ("MINIMUM", r["minimum"])) if on]
        print(f"  #{r['rank']} {r['course']} {r['item']}: score {r1(r['score'])}, "
              f"{float(r['this_week']):g} of {float(r['hours']):g} h this week {' '.join(tags)}")
    for course, f in finals.items():
        print(f"  final needed {course}: earned {f['earned']}, remaining {f['remaining']}, "
              f"target {f['target']} -> {f['verdict']}")


def check_run(case, path):
    text = open(path, encoding="utf-8").read()
    rows, _, finals, _ = plan(case)
    problems = []
    for r in rows:
        line = next((l for l in text.splitlines() if r["item"].lower() in l.lower() and "|" in l
                     and r["course"] in l), "") or next(
            (l for l in text.splitlines() if r["item"].lower() in l.lower() and "|" in l), "")
        no_score_ok = r["stake"] == 0 and re.search(r"\|\s*(n/a|—|-)\s*\|", line)
        if f"{r1(r['score']):.1f}" not in line and not no_score_ok:
            problems.append(f"score for {r['item']} should be {r1(r['score']):.1f}: {line.strip()[:120]!r}")
        if r["start_now"] and "START NOW" not in line.upper():
            problems.append(f"{r['item']} should be tagged START NOW")
    for course, f in finals.items():
        lines = [l for l in text.splitlines() if course in l]
        joined = " ".join(lines)
        if f["verdict"] == "already secured":
            ok = "already secured" in joined.lower()
        elif f["verdict"].startswith("not reachable"):
            ok = "not reachable" in joined.lower() and f"{f['earned'] + f['remaining']:.1f}" in joined
        else:
            n = f"{f['needed']:.1f}"
            ok = n in joined or (n.endswith(".0") and re.search(re.escape(n[:-2]) + r"%", joined))
        if not ok:
            problems.append(f"final needed for {course} should be {f['verdict']}")
    never = text.split("Never minimise", 1)[1][:600] if "Never minimise" in text else ""
    minimum_block = text.split("Safe to do the minimum", 1)[1].split("Never minimise", 1)[0] if "Safe to do the minimum" in text else ""
    for r in rows:
        if r["protected"]:
            if r["item"].lower() not in never.lower():
                problems.append(f"{r['item']} is protected but not under Never minimise")
            rows_in_min = [l for l in minimum_block.splitlines() if l.strip().startswith("|")]
            if any(r["item"].lower() in l.lower() for l in rows_in_min):
                problems.append(f"{r['item']} is protected but on the minimum list")
    print(f"{path}: " + ("OK" if not problems else f"{len(problems)} problem(s)"))
    for p in problems:
        print("  -", p)
    return not problems


def check_ics(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"BEGIN:VCALENDAR.*?END:VCALENDAR", text, re.S)
    if not m:
        print(f"{path}: no .ics block found")
        return False
    lines = [l.strip() for l in m.group(0).splitlines() if l.strip()]
    problems = []
    stack = []
    for l in lines:
        if l.startswith("BEGIN:"):
            stack.append(l[6:])
        elif l.startswith("END:"):
            if not stack or stack.pop() != l[4:]:
                problems.append(f"unbalanced {l}")
    if stack:
        problems.append(f"unclosed {stack}")
    for head in ("VERSION:2.0", "PRODID:"):
        if not any(l.startswith(head) for l in lines):
            problems.append(f"missing {head}")
    events = m.group(0).split("BEGIN:VEVENT")[1:]
    uids = []
    for e in events:
        for prop in ("UID:", "DTSTAMP:", "DTSTART", "SUMMARY:"):
            if prop not in e:
                problems.append(f"event missing {prop}: {e[:60]!r}")
        uid = re.search(r"UID:(\S+)", e)
        if uid:
            uids.append(uid.group(1))
            if not re.fullmatch(r"[A-Za-z0-9-]+@study-easier", uid.group(1)):
                problems.append(f"UID has odd characters: {uid.group(1)}")
        if not re.search(r"DTSTAMP:\d{8}T\d{6}Z", e):
            problems.append("DTSTAMP not in YYYYMMDDTHHMMSSZ form")
        if not re.search(r"DTSTART;TZID=[A-Za-z_]+/[A-Za-z_]+:\d{8}T\d{6}", e):
            problems.append("DTSTART not in TZID=Area/City:YYYYMMDDTHHMMSS form")
    if len(set(uids)) != len(uids):
        problems.append("duplicate UIDs")
    print(f"{path}: {len(events)} events, " + ("ics OK" if not problems else f"{len(problems)} ics problem(s)"))
    for p in problems:
        print("  -", p)
    return not problems


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        for case in CASES:
            show(case)
    elif a[0] == "--ics":
        sys.exit(0 if all(check_ics(p) for p in a[1:]) else 1)
    else:
        sys.exit(0 if check_run(a[0], a[1]) else 1)
