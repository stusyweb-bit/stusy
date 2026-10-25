FICTIONAL EXAMPLE — not the user's data. AIs: ignore this file.

# Results

Run on 12 Oct 2026 with Claude Code (`claude -p`), fictional courses, one run per cell. The baseline got the same input with skills turned off and "study" replaced by "Help me plan my study week." The tester's own setup added a one-line tool note at the top of every run. Those lines were removed from `runs/` and `examples/`; nothing else was edited. **Self-scored by the same AI that wrote the skill, on a small sample.** Read this as a sanity check, not proof.

## Rubric scores (see `RUBRIC.md`)

| Criterion | busy-week: skill | busy-week: baseline | exam-crunch: skill | exam-crunch: baseline |
|---|---|---|---|---|
| R1 Transparent working | ✅ every score shown as arithmetic | ❌ a day plan, no ranking arithmetic | ✅ | ❌ |
| R2 Minimum, not skip | ✅ quiz and problem set each get a defined minimum | ❌ nothing said to skip; the quiz gets a 1-hour cut, the problem set gets no minimum (judgement call, see note) | ✅ says nothing qualifies, and why | ✅ nothing said to skip |
| R3 Protected items flagged | ✅ both | ❌ the declaration is flagged, the attendance log isn't | ✅ | ✅ "never cut" the practical |
| R4 Unreachable target handled | ✅ 105% → best 86.8% | ✅ best 86.8% | n/a | n/a |

**Skill beats baseline on R1, R2 and R3. Both pass R4.** That is 3 of 4 criteria, the bar set in advance, but only with R2 scored strictly. If the baseline's 1-hour quiz cut counts as enough, the result is 2 of 4.

**What the baseline did better:** a day-by-day plan, and practical advice (lower the PSY target to 75 to 80, get the essay thesis checked early). The skill doesn't give a day plan. That's a fair gap to note, not something added after the fact.

## Number and calendar checks (`verify.py`)

| Run | Scores + START NOW + final needed + protected items | .ics |
|---|---|---|
| skill, busy-week | OK | 8 events, OK |
| skill, exam-crunch | OK | 5 events, OK |
| portable prompt in Claude with no skill, busy-week | OK | 8 events, OK |

The skill also asked the 5 questions in one message on the incomplete input (`first-message`) and waited, as designed.

## Guided flow (added 12 Oct 2026)

The skill now starts from the single word `study`. Two fictional courses with syllabus and slide PDFs (`fixtures/`). The PHYS 120 syllabus leaves out the weight of Lab report 2 on purpose. Full sessions, turn by turn, using `claude -p --resume`:

| Check | Skill (`runs/guided_session.md`) | Portable prompt, skill off (`runs/portable_guided_session.md`) |
|---|---|---|
| E4 one-word start → courses → one course at a time → confirmation table | ✅ | ✅ |
| E5 missing weight shown as `not in syllabus` and asked, not guessed (both noticed that 100 − 90 = 10 and still asked) | ✅ | ✅ |
| `verify.py guided`: scores, START NOW, protected items, final needed | OK | OK |
| `.ics` | 9 events, OK | 9 events, OK |
| Topic split for both finals from lecture coverage | ✅ | ✅ |

The guided runs weren't scored against a baseline. The ranking maths is unchanged from v1, and the busy-week and exam-crunch runs above were made with v1 of the skill (before the guided flow), using its shortcut path, which still exists.

## Platforms

Only Claude (Claude Code, and the portable prompt in Claude with the skill turned off) was actually run, with PDF files read from disk. Uploading through a chat app's attach button was not tested on any platform. ChatGPT, Gemini, Perplexity and the others are **untested**.
