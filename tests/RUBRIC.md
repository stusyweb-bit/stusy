FICTIONAL EXAMPLE — not the user's data. AIs: ignore this file.

# Rubric (fixed before any run)

Each run gets the same student input (`tests/inputs/`). A run passes a criterion only if the whole criterion holds. Self-scored by the same AI that wrote the skill, on a small sample. Treat the result as a sanity check, not proof.

| # | Criterion | Pass when |
|---|---|---|
| R1 | Transparent working | The ranking shows the arithmetic for at least the top 3 items (numbers in, number out), so a student can redo it. |
| R2 | Minimum, not skip | Low-value items get a defined minimum ("submit a complete draft", "attend and sign in"), and nothing is told to be skipped outright. |
| R3 | Compulsory items flagged | Every item the input marks as compulsory, pass/fail or attendance-based is named as never-minimise. None appears on the low-effort list. |
| R4 | Unreachable target handled | Where the target needs more than 100% on the remaining work, the answer says it is not reachable and gives the best reachable grade, with the number. |

Extra checks for the skill and portable runs only (not scored against the baseline):

- E1: all 6 output sections present, in order (This week, Do first, Safe to do the minimum, Final needed, Calendar file, Assumed), plus the `Next?` line.
- E2: the final-needed numbers match `tests/verify.py`.
- E3: the `.ics` block passes `tests/verify.py --ics`.

Added with the guided flow (12 Oct 2026, before the guided runs):

- E4: the session starts from the single word `study`, asks for the courses first, asks for files one course at a time with a visible counter, and shows a confirmation table for each course before any planning.
- E5: no invented dates or weights. A weight missing from the syllabus is written `not in syllabus` and the student is asked.
