FICTIONAL EXAMPLE — not the user's data. AIs: ignore this file.

# Example: the guided flow, from one word to a plan

_Walkthrough of the current `stusy` flow on two fictional courses. The files are in [`tests/fixtures/`](../tests/fixtures/). The course data, the student's answers and the plan below come from a real run in Claude Code on the earlier flow ([`tests/runs/guided_session.md`](../tests/runs/guided_session.md)). The opening turns were rewritten on 2026-10-22 to show the new order (name, syllabuses, calendar, then notes); the new flow has not been recorded as a full run yet._

---

**Student:**
> stusy

**stusy:**

Hi! I'm stusy. I'll turn your syllabuses into a calendar and a plan for this week.

What's your name? And how many courses are you taking this term?
(Example: "<your name>, 3")

---

**Student:**
> Alex, 2

**stusy:**

Alex, some courses don't allow AI tools. Check your course's AI policy before uploading its materials.

**Course 1 of 2**
Upload its syllabus (PDF, Word, photos or pasted text all work). You can also give me a file path or a folder.
No syllabus? Type the assessment list with dates and weights instead.

---

**Student:**
> GEOG105_syllabus.pdf (in this folder)

**stusy:**

**Alex, Course 1 of 2: GEOG 105 Urban Geography (3 credits): here's what I found.**

| Item | Weight | Due | Notes |
|---|---|---|---|
| Midterm test | 25% | Fri 16 Oct (in class) | time not in syllabus · coverage not in syllabus: which lectures does it cover? |
| Field journal | 15% | Fri 6 Nov 23:59 | |
| Field trip | 5% | Sat 7 Nov 09:00 | **compulsory**: missing it without a documented reason means you can't pass the course |
| Map assignment | 20% | Wed 11 Nov 17:00 | |
| Final exam | 35% | Thu 3 Dec 09:00 | covers Lectures 6–11 |

Lecture schedule: L1 What makes a city · L2 Urban growth · L3 Land use · L4 Cities and water · L5 Urban climate basics · L10 Housing density · L11 Climate-ready cities (from the syllabus; L6–L9 aren't named in it, your notes can fill them in later)

Is this correct? (ok / fix …) If you know which lectures the midterm covers, or what time it starts, tell me and I'll add it.

---

**Student:**
> ok. The midterm is already done.

**stusy:**

Alex, got it. I've marked the GEOG 105 midterm as finished. It won't be ranked, and it only counts toward `Final needed`.

**Course 2 of 2**
Upload its syllabus (PDF, Word, photos or pasted text all work).
No syllabus? Type the assessment list with dates and weights instead.

---

**Student:**
> PHYS120_syllabus.pdf

**stusy:**

**Alex, Course 2 of 2: PHYS 120 Physics of Everyday Life (4 credits): here's what I found.**

| Item | Weight | Due | Notes |
|---|---|---|---|
| Problem sets 1–3 | 15% (5% each) | done | finished: counts only toward `Final needed` |
| Midterm | 25% | Thu 15 Oct | time not in syllabus · coverage not in syllabus |
| Lab report 1 | 10% | Fri 16 Oct | time not in syllabus |
| Lab safety quiz | pass/fail | Tue 3 Nov 12:00 | **protected**: you must pass it before you can attend any lab |
| Problem set 4 | 5% | Mon 9 Nov 23:59 | |
| Lab report 2 | **not in syllabus** | Fri 13 Nov 17:00 | what is it worth? |
| Problem set 5 | 5% | Mon 16 Nov 23:59 | |
| Final exam | 30% | Tue 1 Dec 14:00 | covers Lectures 1–8 |

Lecture schedule: L1 Motion and speed · L2 Forces · L3 Energy · L4 Heat (from the syllabus; L5–L8 aren't named in it)

Two things to check:
1. **Lab report 2 has no weight.** The other weights add up to 90%, so it may be 10%, but I won't assume that. What does it say on your course site or in the course outline?
2. **Are the midterm (15 Oct) and lab report 1 (16 Oct) done**, like the GEOG midterm?

Is this correct? (ok / fix …)

---

**Student:**
> Lab report 2 is 10%. Yes, the midterm and lab report 1 are done. Everything else ok.

**stusy:**

Alex, here are all your dates.

**October 2026**
| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| | | | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 PHYS Midterm 25% ✓ | 16 GEOG Midterm 25% ✓<br>PHYS Lab report 1 10% ✓ | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 | |

**November 2026**
| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| | | | | | | 1 |
| 2 | 3 PHYS Lab safety quiz P/F ⚑ | 4 | 5 | 6 GEOG Field journal 15% | 7 GEOG Field trip 5% ⚑ | 8 |
| 9 PHYS Problem set 4 5% | 10 | 11 GEOG Map assignment 20% | 12 | 13 PHYS Lab report 2 10% | 14 | 15 |
| 16 PHYS Problem set 5 5% | 17 | 18 | 19 | 20 | 21 | 22 |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 |
| 30 | | | | | | |

**December 2026**
| Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|
| | 1 PHYS Final exam 30% | 2 | 3 GEOG Final exam 35% | 4 | 5 | 6 |
| 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 |
| 28 | 29 | 30 | 31 | | | |

In date order:
- Thu 15 Oct · PHYS 120 · Midterm · 25% ✓
- Fri 16 Oct · GEOG 105 · Midterm test · 25% ✓
- Fri 16 Oct · PHYS 120 · Lab report 1 · 10% ✓
- Tue 3 Nov 12:00 · PHYS 120 · Lab safety quiz · pass/fail ⚑
- Fri 6 Nov 23:59 · GEOG 105 · Field journal · 15%
- Sat 7 Nov 09:00 · GEOG 105 · Field trip · 5% ⚑
- Mon 9 Nov 23:59 · PHYS 120 · Problem set 4 · 5%
- Wed 11 Nov 17:00 · GEOG 105 · Map assignment · 20%
- Fri 13 Nov 17:00 · PHYS 120 · Lab report 2 · 10%
- Mon 16 Nov 23:59 · PHYS 120 · Problem set 5 · 5%
- Tue 1 Dec 14:00 · PHYS 120 · Final exam · 30%
- Thu 3 Dec 09:00 · GEOG 105 · Final exam · 35%

Want it in Google Calendar, Apple Calendar or Outlook? Tell me your time zone and I'll make the .ics file now. Otherwise it comes with your plan.

**Course 1 of 2: GEOG 105 Urban Geography**
Now upload its lecture notes or slides, plus anything else that helps: assignment briefs, a reading list, past papers, exam guidance.
Nothing yet? Type `skip` and I'll plan from the syllabus alone.

---

**Student:**
> GEOG105_slides_L6-L9.pdf

**stusy:**

Alex, GEOG 105: here's what your notes add.
Lecture topics: L6 Urban heat islands · L7 Flooding and drainage · L8 Green infrastructure · L9 Transport and emissions
Final exam coverage: Lectures 6–11 (matches the syllabus)
Nothing in them changes a date or a weight.
Correct? (ok / fix …)

---

**Student:**
> ok

**stusy:**

**Alex, Course 2 of 2: PHYS 120 Physics of Everyday Life**
Now upload its lecture notes or slides, plus anything else that helps: assignment briefs, a reading list, past papers, exam guidance.
Nothing yet? Type `skip` and I'll plan from the syllabus alone.

---

**Student:**
> PHYS120_slides_L5-L8.pdf

**stusy:**

Alex, PHYS 120: here's what your notes add.
Lecture topics: L5 Waves and sound · L6 Light · L7 Electricity at home · L8 Magnets and motors
Final exam coverage: Lectures 1–8 (matches the syllabus)
Nothing in them changes a date or a weight.
Correct? (ok / fix …)

---

**Student:**
> ok

**stusy:**

Alex, last questions. Reply `ok` to accept a default:

1. **What's today's date, and what time zone are you in?** (no default: I need an answer here. My system clock says 12 Oct, but you've already sat midterms dated 15 and 16 Oct, so I won't trust it.)
2. **How many hours can you study this week?** (default: 15)
3. **How many hours will each item take?** (defaults: lab safety quiz 2 · problem sets 4 and 5, 6 each · field journal 6 · lab report 2, 10 · map assignment 6 · each final exam 15 · field trip 4)
4. **What marks have you had so far, and what grade are you aiming for in each course?** Only needed for `Final needed`. Finished items: GEOG midterm (25%) · PHYS problem sets 1–3 (5% each) · PHYS midterm (25%) · PHYS lab report 1 (10%). (default: skip that section)
5. **Is anything else compulsory that the syllabuses didn't mention?** (default: only what they say, which is the GEOG field trip and the PHYS lab safety quiz)

---

**Student:**
> 1) Monday 2 November 2026, Asia/Singapore. 2) 18 hours. 3) safety quiz 0.5, problem sets 3 each, field journal 4, lab report 2 6, map assignment 6, finals 15 each, field trip 4. 4) GEOG midterm 72%, target 75. PHYS problem sets 1-3 average 90%, midterm 81%, lab report 1 78%, target 85. 5) ok

**stusy:**

Alex, here's your week.

**Week of:** Mon 2 Nov 2026 (Asia/Singapore) · **Hours you have:** 18 · **Planned:** 18

### This week
| Rank | Course | Item | Due | Weight | Hours | Score | Why |
|---|---|---|---|---|---|---|---|
| 1 | PHYS 120 | Lab safety quiz | Tue 3 Nov 12:00 | pass/fail | 0.5 | n/a | START NOW: due tomorrow, and you can't go to labs until you pass it |
| 2 | GEOG 105 | Field journal | Fri 6 Nov 23:59 | 15% | 4 | 5.6 | due in 4 days, highest score |
| 3 | PHYS 120 | Problem set 4 | Mon 9 Nov 23:59 | 5% | 3 | 3.3 | due in 7 days |
| 4 | GEOG 105 | Map assignment | Wed 11 Nov 17:00 | 20% | 6 | 3.3 | ties with #3, due later |
| 5 | PHYS 120 | Lab report 2 | Fri 13 Nov 17:00 | 10% | 6 → 0.5 this week | 2.2 | the rest is next week |
| 6 | PHYS 120 | Problem set 5 | Mon 16 Nov 23:59 | 5% | 3 → next week | 2.2 | ties with #5, due later |
| 7 | GEOG 105 | Field trip | Sat 7 Nov 09:00 | 5% | 4 | 1.9 | compulsory: you can't pass GEOG without it |
| 8 | PHYS 120 | Final exam | Tue 1 Dec 14:00 | 30% | 15 → next week | 1.3 | 29 days left |
| 9 | GEOG 105 | Final exam | Thu 3 Dec 09:00 | 35% | 15 → next week | 1.2 | 31 days left |

The table is in score order. Hours were given in a different order: first everything due within 7 days (#1, #2, #3, #7 = 11.5 h), then later items by rank (#4 gets 6 h, #5 gets 0.5 h). That adds up to 18 h.

Working (PHYS has 4 credits, so its stake is multiplied by 4 ÷ 3):
- `#1 Lab safety quiz: pass/fail, so no score · latest start = 3 Nov − ceil(0.5 × 7 ÷ 18) = 3 Nov − 1 = 2 Nov (today) → START NOW`
- `#2 Field journal: 15 × 1.5 ÷ 4 = 5.6`
- `#3 Problem set 4: 5 × 4/3 = 6.67 · 6.67 × 1.5 ÷ 3 = 3.3`
- `#4 Map assignment: 20 × 1 ÷ 6 = 3.3`
- `#5 Lab report 2: 10 × 4/3 = 13.33 · 13.33 × 1 ÷ 6 = 2.2`
- `#6 Problem set 5: 6.67 × 1 ÷ 3 = 2.2`
- `#7 Field trip: 5 × 1.5 ÷ 4 = 1.9`
- `#8 PHYS final: 30 × 4/3 = 40 · 40 × 0.5 ÷ 15 = 1.3`
- `#9 GEOG final: 35 × 0.5 ÷ 15 = 1.2`

Topic split:
- `GEOG final (15 h ÷ 6 lectures): L6 Urban heat islands 2.5 h · L7 Flooding and drainage 2.5 h · L8 Green infrastructure 2.5 h · L9 Transport and emissions 2.5 h · L10 Housing density 2.5 h · L11 Climate-ready cities 2.5 h`
- `PHYS final (15 h ÷ 8 lectures): L1 Motion and speed · L2 Forces · L3 Energy · L4 Heat · L5 Waves and sound · L6 Light · L7 Electricity at home · L8 Magnets and motors · 1.875 h each`
- `Lab safety quiz: coverage not in syllabus`

### Do first
1. **Lab safety quiz.** First 25 minutes: open the quiz page on your course site, note the time limit and whether you can retake it, and block 30 minutes before 12:00 tomorrow to sit it.
2. **Field journal.** First 25 minutes: open the brief, list every required entry and the marking criteria, and tick off the entries you've already written.
3. **Problem set 4.** First 25 minutes: read every question and mark each one `can do`, `need notes` or `stuck`.

### Safe to do the minimum
Nothing qualifies: every low scorer is either worth too much or protected. The median score is 2.2. The three items below it are the field trip (protected), the PHYS final (stake 40) and the GEOG final (stake 35).

**Never minimise:** GEOG 105 field trip (compulsory: missing it without a documented reason means you can't pass the course) · PHYS 120 lab safety quiz (pass/fail, and you need it to attend labs, including the lab for lab report 2)

### Final needed
| Course | Earned so far | Remaining | Target | Needed on the rest |
|---|---|---|---|---|
| GEOG 105 | 18.0 | 75% | 75 | 76% · best reachable 93% |
| PHYS 120 | 41.55 | 50% | 85 | 86.9% · best reachable 91.55% |

Working:
- `GEOG: earned = 25 × 0.72 = 18 · remaining = 100 − 25 = 75 · (75 − 18) ÷ 75 × 100 = 76%`
- `PHYS: earned = 15 × 0.90 + 25 × 0.81 + 10 × 0.78 = 13.5 + 20.25 + 7.8 = 41.55 · remaining = 100 − 50 = 50 · (85 − 41.55) ÷ 50 × 100 = 86.9%`

### Calendar file
I can't write files in this session. Copy this into a text file named study.ics, then import it into Google Calendar, Apple Calendar or Outlook.

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//study_easier//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:PHYS120-lab-safety-quiz-20261103@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261103T120000
DURATION:PT15M
SUMMARY:DUE PHYS 120 · Lab safety quiz (pass/fail)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:GEOG105-field-journal-20261106@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261106T235900
DURATION:PT15M
SUMMARY:DUE GEOG 105 · Field journal (15%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:GEOG105-field-trip-20261107@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261107T090000
DURATION:PT15M
SUMMARY:DUE GEOG 105 · Field trip, compulsory (5%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:PHYS120-problem-set-4-20261109@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261109T235900
DURATION:PT15M
SUMMARY:DUE PHYS 120 · Problem set 4 (5%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:GEOG105-map-assignment-20261111@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261111T170000
DURATION:PT15M
SUMMARY:DUE GEOG 105 · Map assignment (20%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:PHYS120-lab-report-2-20261113@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261113T170000
DURATION:PT15M
SUMMARY:DUE PHYS 120 · Lab report 2 (10%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:PHYS120-problem-set-5-20261116@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261116T235900
DURATION:PT15M
SUMMARY:DUE PHYS 120 · Problem set 5 (5%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:PHYS120-final-exam-20261201@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261201T140000
DURATION:PT15M
SUMMARY:DUE PHYS 120 · Final exam (30%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:GEOG105-final-exam-20261203@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261203T090000
DURATION:PT15M
SUMMARY:DUE GEOG 105 · Final exam (35%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
END:VCALENDAR
```

### Assumed
- The hours for each item are your estimates, not defaults.
- The lab safety quiz is pass/fail, so it has no score. It was placed first because of the start-now check.
- Lab report 2 is worth 10%, from you, not the syllabus.
- Lab safety quiz coverage is not in the syllabus.
- The field trip's "due" time is its 09:00 start.
- Compulsory items are only the ones the syllabuses list (you said ok).
- PHYS problem sets 1–3 use your 90% average for all three.

Ranking is a heuristic. Check it against your syllabus.

Next? (shift a deadline / add a course / calendar / just the .ics / done)
