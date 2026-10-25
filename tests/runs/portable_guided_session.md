FICTIONAL EXAMPLE — not the user's data. AIs: ignore this file.

# Guided session: portable prompt

_Real multi-turn run in Claude Code (`claude -p` with `--resume`, Skill tool disabled), 12 Oct 2026, fictional courses from `tests/fixtures/`. The student turns are typed exactly as shown._


=== STUDENT:
[the prompt from PORTABLE.md, pasted as the first message]

=== ASSISTANT:
Ready. Type **study** when you want to start.


=== STUDENT:
study

=== ASSISTANT:
How many courses are you taking this term, and what are they called?


=== STUDENT:
2: GEOG 105 Urban Geography and PHYS 120 Physics of Everyday Life

=== ASSISTANT:
Some courses don't allow AI tools. Check your course's AI policy before uploading its materials.

Course 1 of 2: GEOG 105 Urban Geography. Upload its syllabus and lecture slides (PDF, PowerPoint, photos or pasted text). No slides yet? Just send the syllabus.


=== STUDENT:
Here they are: GEOG105_syllabus.pdf and GEOG105_slides_L6-L9.pdf (in this folder)

=== ASSISTANT:
**GEOG 105 Urban Geography**: 3 credits, Fall 2026

| Item | Weight | Due | Notes |
|---|---|---|---|
| Midterm test | 25% | Fri 16 Oct (in class) | Time not in syllabus (lectures are Mondays 10:00, but this is a Friday). Lecture coverage not in syllabus. |
| Field journal | 15% | Fri 6 Nov, 23:59 | |
| Field trip | 5% | Sat 7 Nov, 09:00 | **Compulsory.** If you miss it without a documented reason, you cannot pass the course. |
| Map assignment | 20% | Wed 11 Nov, 17:00 | |
| Final exam | 35% | Thu 3 Dec, 09:00 | Covers L6–L11 |

Weights total: 25 + 15 + 5 + 20 + 35 = 100%

**Lecture topics**
| Lecture | Date | Topic |
|---|---|---|
| L1 | Mon 7 Sep | What makes a city |
| L2 | Mon 14 Sep | Urban growth |
| L3 | Mon 21 Sep | Land use |
| L4 | Mon 28 Sep | Cities and water |
| L5 | Mon 5 Oct | Urban climate basics |
| L6 | Mon 19 Oct | Urban heat islands |
| L7 | Mon 26 Oct | Flooding and drainage |
| L8 | Mon 2 Nov | Green infrastructure |
| L9 | Mon 9 Nov | Transport and emissions |
| L10 | Mon 16 Nov | Housing density |
| L11 | Mon 23 Nov | Climate-ready cities |

The syllabus doesn't give the midterm's start time or which lectures it covers. Do you know either one?

Correct? (ok / fix ...)


=== STUDENT:
ok. The midterm is already done.

=== ASSISTANT:
Noted. The GEOG 105 midterm (25%) is marked as finished, so it will only count in "Final needed".

Course 2 of 2: PHYS 120 Physics of Everyday Life. Upload its syllabus and lecture slides (PDF, PowerPoint, photos or pasted text). No slides yet? Just send the syllabus.


=== STUDENT:
PHYS120_syllabus.pdf and PHYS120_slides_L5-L8.pdf

=== ASSISTANT:
**PHYS 120 Physics of Everyday Life**: 4 credits, Fall 2026

| Item | Weight | Due | Notes |
|---|---|---|---|
| Problem sets 1–3 | 15% (5% each) | done | Your marks are needed for "Final needed" |
| Problem set 4 | 5% | Mon 9 Nov, 23:59 | |
| Problem set 5 | 5% | Mon 16 Nov, 23:59 | |
| Midterm | 25% | Thu 15 Oct | Time not in syllabus. Lecture coverage not in syllabus. |
| Lab report 1 | 10% | Fri 16 Oct | Time not in syllabus |
| Lab report 2 | **not in syllabus** | Fri 13 Nov, 17:00 | Weight missing |
| Lab safety quiz | Pass/fail | Tue 3 Nov, 12:00 | **Compulsory gate.** You must pass it before you can attend any lab session. |
| Final exam | 30% | Tue 1 Dec, 14:00 | Covers L1–L8 |

The listed weights total 15 + 5 + 5 + 25 + 10 + 30 = 90%. That leaves 100 − 90 = 10%, but the syllabus doesn't give Lab report 2 a weight, so I won't assume one.

**Lecture topics**
| Lecture | Date | Topic |
|---|---|---|
| L1 | Tue 8 Sep | Motion and speed |
| L2 | Tue 15 Sep | Forces |
| L3 | Tue 22 Sep | Energy |
| L4 | Tue 29 Sep | Heat |
| L5 | Tue 6 Oct | Waves and sound |
| L6 | Tue 13 Oct | Light |
| L7 | Tue 20 Oct | Electricity at home |
| L8 | Tue 27 Oct | Magnets and motors |

Questions:
- What is Lab report 2's weight?
- Do you know the time of the Midterm and Lab report 1, and which lectures the Midterm covers?

Correct? (ok / fix ...)


=== STUDENT:
Lab report 2 is 10%. Yes, the midterm and lab report 1 are done. Everything else ok.

=== ASSISTANT:
Noted: Lab report 2 is 10%, and the PHYS 120 Midterm (25%) and Lab report 1 (10%) are finished. PHYS 120 weights now total 90 + 10 = 100%.

Please answer these, or reply "ok" to accept a default:

1) **Today's date and time zone?** (no default, you must answer)
2) **Study hours you have this week?** (default 15)
3) **Hours each item will take?** (defaults: quiz 2, assignment 6, presentation 8, report or essay 10, exam revision 15, other 4)
   My mapping: GEOG Field journal = report 10 · GEOG Map assignment = assignment 6 · GEOG Final exam = exam revision 15 · PHYS Problem sets 4 and 5 = assignment 6 each · PHYS Lab report 2 = report 10 · PHYS Lab safety quiz = quiz 2 · PHYS Final exam = exam revision 15 · GEOG Field trip = other 4
4) **Marks so far and target grade per course?** Finished items: GEOG Midterm; PHYS Problem sets 1–3, Midterm, Lab report 1. (default: skip Final needed)
5) **Anything compulsory the syllabus didn't say?** (default: none)


=== STUDENT:
1) Monday 2 November 2026, Asia/Singapore. 2) 18 hours. 3) safety quiz 0.5, problem sets 3 each, field journal 4, lab report 2 6, map assignment 6, finals 15 each, field trip 4. 4) GEOG midterm 72%, target 75. PHYS problem sets 1-3 average 90%, midterm 81%, lab report 1 78%, target 85. 5) ok

=== ASSISTANT:
**Week of:** Mon 2 Nov 2026 (Asia/Singapore)
**Hours I have:** 18
**Hours planned:** 0.5 + 4 + 3 + 4 + 6 + 0.5 = 18

## This week

| Rank | Course | Item | Due | Weight | Hours | Score | Why |
|---|---|---|---|---|---|---|---|
| 1 | PHYS 120 | Lab safety quiz | Tue 3 Nov 12:00 | Pass/fail | 0.5 of 0.5 | 0.0 | **START NOW**. Due in 1 day, and you can't attend labs without passing it. |
| 2 | GEOG 105 | Field journal | Fri 6 Nov 23:59 | 15% | 4 of 4 | 5.6 | Highest score, due in 4 days |
| 3 | PHYS 120 | Problem set 4 | Mon 9 Nov 23:59 | 5% | 3 of 3 | 3.3 | Due in 7 days. Ties Map; earlier due date wins. |
| 4 | GEOG 105 | Field trip | Sat 7 Nov 09:00 | 5% | 4 of 4 | 1.9 | Due in 5 days. Compulsory to pass the course. |
| 5 | GEOG 105 | Map assignment | Wed 11 Nov 17:00 | 20% | 6 of 6 | 3.3 | Top-ranked of the items due after 7 days |
| 6 | PHYS 120 | Lab report 2 | Fri 13 Nov 17:00 | 10% | 0.5 of 6 | 2.2 | Gets the last 0.5 h. Ties PS5; earlier due date wins. |
| next week | PHYS 120 | Lab report 2 (rest) | Fri 13 Nov 17:00 | 10% | 5.5 | 2.2 | |
| next week | PHYS 120 | Problem set 5 | Mon 16 Nov 23:59 | 5% | 3 | 2.2 | |
| next week | PHYS 120 | Final exam | Tue 1 Dec 14:00 | 30% | 15 | 1.3 | |
| next week | GEOG 105 | Final exam | Thu 3 Dec 09:00 | 35% | 15 | 1.2 | |

**Fill order:** Items due within 7 days come first: Safety quiz 0.5 (START NOW), Field journal 4, PS4 3, Field trip 4. That uses 11.5 h, so 18 − 11.5 = 6.5 h are left. Then later items by rank: Map 6, leaving 0.5 h for Lab report 2.

**Working** (stake = weight × credits/3; GEOG has 3 credits so ×1, PHYS has 4 credits so ×4/3):
- Field journal: days 6 − 2 = 4 → urgency 1.5. Score 15 × 1 × 1.5 / 4 = 5.6. Latest start 4 × 7 / 18 = 1.56 → 2 days → 4 Nov (not today).
- PS4: days 9 − 2 = 7 → urgency 1.5. Stake 5 × 4/3 = 6.67. Score 6.67 × 1.5 / 3 = 3.3. Latest start 3 × 7 / 18 = 1.17 → 2 → 7 Nov.
- Map assignment: days 11 − 2 = 9 → urgency 1. Score 20 × 1 × 1 / 6 = 3.3. Latest start 6 × 7 / 18 = 2.33 → 3 → 8 Nov.
- Lab report 2: days 13 − 2 = 11 → urgency 1. Stake 10 × 4/3 = 13.33. Score 13.33 × 1 / 6 = 2.2. Latest start 3 days → 10 Nov.
- PS5: days 16 − 2 = 14 → urgency 1. Stake 6.67. Score 6.67 × 1 / 3 = 2.2. Latest start 2 days → 14 Nov.
- Field trip: days 7 − 2 = 5 → urgency 1.5. Score 5 × 1 × 1.5 / 4 = 1.9. Latest start 2 days → 5 Nov.
- PHYS final: days (30 − 2) + 1 = 29 → urgency 0.5. Stake 30 × 4/3 = 40. Score 40 × 0.5 / 15 = 1.3. Latest start 15 × 7 / 18 = 5.83 → 6 → 25 Nov.
- GEOG final: days (30 − 2) + 3 = 31 → urgency 0.5. Score 35 × 1 × 0.5 / 15 = 1.2. Latest start 6 days → 27 Nov.
- Lab safety quiz: days 3 − 2 = 1 → urgency 3. Stake 0 (pass/fail, no weight). Score 0 × 3 / 0.5 = 0.0. Latest start 0.5 × 7 / 18 = 0.19 → 1 day → 3 − 1 = 2 Nov = today → **START NOW**.

**Topic split**
- PHYS Lab safety quiz: coverage not in syllabus
- GEOG Final exam (next week), 15 / 6 lectures = 2.5 h each: L6 Urban heat islands 2.5 h · L7 Flooding and drainage 2.5 h · L8 Green infrastructure 2.5 h · L9 Transport and emissions 2.5 h · L10 Housing density 2.5 h · L11 Climate-ready cities 2.5 h
- PHYS Final exam (next week), 15 / 8 lectures = 1.875 h each: L1 Motion and speed · L2 Forces · L3 Energy · L4 Heat · L5 Waves and sound · L6 Light · L7 Electricity at home · L8 Magnets and motors (1.875 h each)

## Do first
1. **PHYS Lab safety quiz** (START NOW, due Tue 3 Nov 12:00): Open the quiz page. Note the time limit, number of attempts and pass mark. Collect the safety material it's based on. Then block a time to take it before 12:00 tomorrow.
2. **GEOG Field journal** (due Fri 6 Nov 23:59): Open the journal brief. List every required entry or section, and mark each one done, partly done or not started.
3. **PHYS Problem set 4** (due Mon 9 Nov 23:59): Open PS4 and read every question. Tag each one "can do", "need lecture N" or "stuck", and put the "stuck" ones on your list for office hours.

## Safe to do the minimum

None qualify. The median score is 2.2 (sorted: 0.0, 1.2, 1.3, 1.9, **2.2**, 2.2, 3.3, 3.3, 5.6). These four score below it:
- GEOG Final exam (1.2): stake 35, over 5
- PHYS Final exam (1.3): stake 40, over 5
- Lab safety quiz (0.0): protected
- Field trip (1.9): protected

| Item | Minimum | Hours saved |
|---|---|---|
| none | none | 0 |

**Never minimise:**
- GEOG 105 Field trip, Sat 7 Nov 09:00. Attendance is compulsory, and missing it without a documented reason means you cannot pass the course.
- PHYS 120 Lab safety quiz, Tue 3 Nov 12:00. It's pass/fail, and you must pass it to attend any lab session.

## Final needed

| Course | Earned | Remaining | Target | Needed |
|---|---|---|---|---|
| GEOG 105 | 18.0 | 75 | 75 | 76.0% (best reachable 93.0) |
| PHYS 120 | 41.55 | 50 | 85 | 86.9% (best reachable 91.55) |

- GEOG 105: earned = 25 × 0.72 = 18.0. Remaining = 100 − 25 = 75. Needed = (75 − 18.0) / 75 × 100 = 57 / 75 × 100 = 76.0%. Best reachable = 18.0 + 75 = 93.0.
- PHYS 120: earned = 15 × 0.90 + 25 × 0.81 + 10 × 0.78 = 13.5 + 20.25 + 7.8 = 41.55. Remaining = 100 − (15 + 25 + 10) = 50. Needed = (85 − 41.55) / 50 × 100 = 43.45 / 50 × 100 = 86.9%. Best reachable = 41.55 + 50 = 91.55.

## Calendar file

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//study_easier//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:phys120-lab-safety-quiz-20261103@study-easier
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
UID:geog105-field-journal-20261106@study-easier
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
UID:geog105-field-trip-20261107@study-easier
DTSTAMP:20261102T000000Z
DTSTART;TZID=Asia/Singapore:20261107T090000
DURATION:PT15M
SUMMARY:DUE GEOG 105 · Field trip (5%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:phys120-problem-set-4-20261109@study-easier
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
UID:geog105-map-assignment-20261111@study-easier
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
UID:phys120-lab-report-2-20261113@study-easier
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
UID:phys120-problem-set-5-20261116@study-easier
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
UID:phys120-final-exam-20261201@study-easier
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
UID:geog105-final-exam-20261203@study-easier
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

Copy this into a text file named study.ics and import it into your calendar.

## Assumed
- The week runs Mon 2 Nov to Sun 8 Nov 2026. "Due within 7 days" means 7 days left or fewer, so PS4 counts.
- All item hours are yours: safety quiz 0.5, problem sets 3 each, field journal 4, lab report 2 6, map assignment 6, finals 15 each, field trip 4. No default hours were used.
- The lab safety quiz has stake 0 because it is pass/fail with no weight. It is placed by START NOW, not by score.
- PHYS problem sets 1–3 are scored at 90% each, from your average. They are weighted equally at 5% each.
- Lab report 2 is 10%, as you said; the syllabus left it blank.
- GEOG midterm and PHYS midterm and lab report 1 are finished, as you said.
- Nothing compulsory beyond the syllabus (default).
- All due times come from the syllabus, so the 23:59 default wasn't needed.

Ranking is a heuristic. Check it against your syllabus.

Next? (shift a deadline / add a course / just the .ics / done)
