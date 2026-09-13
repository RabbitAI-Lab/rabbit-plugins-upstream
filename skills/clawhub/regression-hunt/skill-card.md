## Description:

Find what a change can break in code that did not change by tracing a diff, branch, commit range, or feature outward through callers, consumers, shared state, and contracts, then ranking concrete regression scenarios and proving or clearing them with observed test runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to assess the regression risk of code changes by tracing affected surfaces beyond the modified lines and checking each candidate with observed tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read code broadly, run tests, and add focused tests while checking regression candidates.

Mitigation: Run it in the intended repository workspace and review any proposed commands or test edits before accepting them.

Risk: Regression conclusions can be misleading if a path is not fully traced or a test result was not observed.

Mitigation: Require cited searches, file references, and quoted test summaries; keep unobserved paths labeled as suspected or not run.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown report with cited file paths, command summaries, and optional focused test changes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses fixed report sections for verdict, confirmed regressions, suspected regressions, cleared paths, coverage, and follow-up offers.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
