# Worked examples

Contents:

- a capacity read that fails and what to do about it
- a rotation designed well and the same rotation designed badly

## Worked capacity read

From curl's publicly described security-triage situation - real and citable, not because most projects look like curl, but because the arithmetic shape transfers.

**What the baseline says.**

- A seven-person volunteer team.
- Each report costs 30 minutes to 3 hours and typically pulls in three to four people.
- Volunteers have around three hours a week.
- Roughly two machine-generated junk reports arrive weekly, and by mid-2025 only about one submission in twenty was genuine.

**The arithmetic.** Seven people × 3 hours = 21 person-hours a week at the optimistic end. Two junk reports a week, at the midpoint of the cost range with three people pulled into each, consume 2 × 1.75 × 3 ≈ 10.5 person-hours - half the team's weekly budget spent on submissions with no valid content, before a single real vulnerability is looked at.

**Reading it back to the user.** "Your capacity is not the problem and your labels are definitely not the problem. Half your available hours are consumed by submissions that were never valid. No response target you publish will survive that, so the design question is which lever you pull on intake."

**The lever chosen.** curl removed the monetary reward entirely, which changed the economics of submitting rather than the cost of evaluating.

This is not:

- a better classifier
- a stricter template
- a faster triage rotation

When the valid share collapses, the intervention has to act on inflow.

**The general form.**

1. Compute weekly person-hours.
2. Subtract the hours consumed by items that will never be actionable.
3. Compare what remains against genuine inflow.

If the remainder is negative, no amount of process design closes the gap: say so plainly and move to the intake and gating decisions in steps 2 and 4.

## Rotation design: a positive and a negative example

Both are documented projects. The negative one matters more: it is the failure a maintainer walks into while believing the problem is solved.

### Negative - the rotation that exists only on paper

Fedora's BugZappers were a real, well-built triage programme:

- a named volunteer and staff team
- a documented charter
- dedicated tooling
- a biweekly meeting with published minutes

Everything step 5 asks for was present. The project's own joining page now states the group is dormant and little triage is happening.

That is worse than never having had a rotation: the documentation still advertises coverage.

- Reporters expect a response that will not come.
- A contributor who wants to help finds a process to join rather than a gap to fill.
- Maintainers cannot see the failure from inside, because every artefact still exists.

**The mistake:** treating "we wrote down the rotation" as the finish line. A rotation decays silently because no error is raised when a shift is skipped.

### Positive - the rotation that cannot silently decay

Mozilla's two-tier model (step 5) survives because its mechanics are automated, not documented: the rotation lives on a shared calendar and a bot syncs the tracker's triage-owner field to whoever is on duty. Requests route to the person actually working this week, instead of accumulating on one name.

Three properties follow:

- A named owner per component prevents diffusion of responsibility.
- Owner-accountable/rotation-executing keeps the owner from becoming the single point of work.
- A named backup per shift stops a skipped week passing unnoticed.

**The contrast in one line:** Fedora documented who _should_ triage; Mozilla automated who _is_ triaging.

### Applying this

Add a liveness check the project can see: a named backup per shift, and one metric that would move if the rotation stopped. If nothing changes on the dashboard when the rota lapses, the rota is documentation, not a process.
