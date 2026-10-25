FICTIONAL EXAMPLE — not the user's data. AIs: ignore this file.

**Week of:** Thu 3 Dec 2026 · **Hours you have:** 45 · **Planned:** 42

### This week
| Rank | Course | Item | Due | Weight | Hours | Score | Why |
|---|---|---|---|---|---|---|---|
| 1 | PHIL 110 | Response paper 6 | Fri 4 Dec 23:59 | 4% | 2 | 6.0 | START NOW: due in 1 day |
| 2 | BIO 140 | Lab practical | Tue 8 Dec 14:00 | 10% pass/fail | 3 | 5.0 | Protected: you must pass it to pass BIO 140 |
| 3 | PHIL 110 | Take-home essay | Mon 7 Dec 23:59 | 30% | 10 | 4.5 | PHIL needs 80.8% on the rest; your average is 72% |
| 4 | BIO 140 | Poster | Thu 10 Dec 17:00 | 20% | 7 | 4.3 | Your BIO target is already met on points, so this raises the grade above 60 |
| 5 | CHEM 150 | Final exam | Mon 7 Dec 09:30 | 45% | 20 | 3.4 | START NOW: needs 4 days at 6.4 h/day. You need 73.9%; your average is 85% |

Working (score = weight × urgency ÷ hours; all courses are 3 credits, so stake = weight; urgency is 3 for 1 day left and 1.5 for 4–7 days left):
- `#1 Response paper 6: 4 × 3 ÷ 2 = 6.0 · latest start = 4 Dec − ceil(2 × 7 ÷ 45 = 0.3) = Thu 3 Dec → START NOW`
- `#2 Lab practical: 10 × 1.5 ÷ 3 = 5.0 · latest start = 8 Dec − ceil(3 × 7 ÷ 45 = 0.5) = Mon 7 Dec`
- `#3 Essay: 30 × 1.5 ÷ 10 = 4.5 · latest start = 7 Dec − ceil(10 × 7 ÷ 45 = 1.6) = Sat 5 Dec`
- `#4 Poster: 20 × 1.5 ÷ 7 = 4.3 · latest start = 10 Dec − ceil(7 × 7 ÷ 45 = 1.1) = Tue 8 Dec`
- `#5 CHEM final: 45 × 1.5 ÷ 20 = 3.4 · latest start = 7 Dec − ceil(20 × 7 ÷ 45 = 3.1) = Thu 3 Dec → START NOW`
- `Load check: due by Mon 23:59 = 2 + 20 + 10 = 32 h · Thu–Mon = 5 days × 6.4 h = 32 h → no spare time until Monday night`
- `Before the exam: Thu–Sun = 4 days × 6.4 h = 25.7 h, minus CHEM 20 h and the response paper 2 h = about 4 h of essay before Monday. The other ~6 h of the essay go on Mon after 09:30`
- `After Monday: lab practical + poster = 3 + 7 = 10 h, and Tue–Thu gives about 19 h`

### Do first
1. **PHIL Response paper 6** (START NOW): first 25 minutes → open the prompt and rubric, write the question in one line in your own words, and list the readings it points to.
2. **CHEM 150 Final** (START NOW): first 25 minutes → open the syllabus topic list, write every exam topic on one page, and mark each one red, amber or green. Your first full revision block starts on the reddest topic.
3. **PHIL Essay** (shares the Mon deadline and there's no spare time before it): first 25 minutes → open the essay brief, copy the marking criteria into a list, and choose your question.

### Safe to do the minimum
Nothing qualifies: every low scorer is either worth too much or protected. (The median score is 4.5. The two below it are the poster, worth 20%, and the CHEM final, worth 45%. Both are above the 5% limit.)

**Never minimise:** BIO 140 Lab practical (pass/fail, and you must pass it to pass the course).

### Final needed
| Course | Earned so far | Remaining | Target | Needed on the rest |
|---|---|---|---|---|
| CHEM 150 | 46.75 | 45% | 80 | 73.9% (best reachable 91.75%) |
| BIO 140 | 61.6 | 30% | 60 | **already secured, but only if you pass the lab practical** |
| PHIL 110 | 47.52 | 34% | 75 | 80.8% (best reachable 81.52%) |

Working:
- `CHEM 150: 55 × 0.85 = 46.75 · (80 − 46.75) ÷ 45 × 100 = 73.9%`
- `BIO 140: 70 × 0.88 = 61.6 · (60 − 61.6) ÷ 30 × 100 = −5.3% → already secured on points; the lab practical still decides whether you pass the course`
- `PHIL 110: 66 × 0.72 = 47.52 · (75 − 47.52) ÷ 34 × 100 = 80.8% · best reachable = 47.52 + 34 = 81.52%`

### Calendar file
This session has no file-writing tool, so here's the file as text:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//study_easier//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
UID:PHIL110-ResponsePaper6-20261204@study-easier
DTSTAMP:20261203T000000Z
DTSTART;TZID=Asia/Hong_Kong:20261204T235900
DURATION:PT15M
SUMMARY:DUE PHIL 110 · Response paper 6 (4%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:CHEM150-FinalExam-20261207@study-easier
DTSTAMP:20261203T000000Z
DTSTART;TZID=Asia/Hong_Kong:20261207T093000
DURATION:PT15M
SUMMARY:DUE CHEM 150 · Final exam (45%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:PHIL110-TakeHomeEssay-20261207@study-easier
DTSTAMP:20261203T000000Z
DTSTART;TZID=Asia/Hong_Kong:20261207T235900
DURATION:PT15M
SUMMARY:DUE PHIL 110 · Take-home essay (30%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:BIO140-LabPractical-20261208@study-easier
DTSTAMP:20261203T000000Z
DTSTART;TZID=Asia/Hong_Kong:20261208T140000
DURATION:PT15M
SUMMARY:DUE BIO 140 · Lab practical (10% pass/fail)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
BEGIN:VEVENT
UID:BIO140-Poster-20261210@study-easier
DTSTAMP:20261203T000000Z
DTSTART;TZID=Asia/Hong_Kong:20261210T170000
DURATION:PT15M
SUMMARY:DUE BIO 140 · Poster (20%)
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:Due in 24 hours
TRIGGER:-PT24H
END:VALARM
END:VEVENT
END:VCALENDAR
```

Copy this into a text file named study.ics, then import it into Google Calendar, Apple Calendar or Outlook.

### Assumed
- Today is Thu 3 Dec 2026, Asia/Hong_Kong, as you said. My system clock reads 12 Oct 2026, so I used your date.
- The hours per item are yours. I spread 45 h evenly over the week, which is 6.4 h a day, and didn't count the 3 h you have spare (45 − 42).
- Your "average so far" is treated as a weighted average over the finished part of each course.
- I don't know how the pass/fail lab practical turns into points. It doesn't affect your BIO target, because finished work alone gives 61.6 ≥ 60.
- The time you spend sitting the CHEM exam isn't counted in your 45 study hours.

Ranking is a heuristic. Check it against your syllabus.

Next? (shift a deadline / add a course / just the .ics / done)
