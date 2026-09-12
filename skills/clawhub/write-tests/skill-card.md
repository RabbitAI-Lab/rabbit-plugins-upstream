## Description:

Helps agents add regression-focused tests by ranking risky behavior, matching project conventions, proving new tests can fail, and reporting covered gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide an agent through writing meaningful tests for new, changed, or legacy code. It emphasizes risk-ranked behavior selection, observable assertions, project-local test conventions, and proof that each new test can fail for the intended reason.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read source files, run project test commands, and edit tests or code while carrying out user-directed test-writing work.

Mitigation: Review the resulting diff and command summaries before accepting changes, especially when behavior was temporarily broken to prove a test can fail.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with inline code, file references, and shell command summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include test files, code edits, command output summaries, coverage gaps, and risk-ranked behavior notes.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
