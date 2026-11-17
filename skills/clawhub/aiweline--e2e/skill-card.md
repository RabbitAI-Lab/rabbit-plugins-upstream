## Description:

E2E automation engineer skill for Playwright-driven flow validation, browser interaction coverage, and end-to-end regression checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiweline](https://clawhub.ai/user/aiweline)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to validate real browser journeys for multi-step UI paths, cross-page interactions, and integration behavior that unit tests cannot prove alone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing login, seed data, target flow, or runtime prerequisites can make browser-flow results incomplete or misleading.

Mitigation: Provide the required test inputs and expected success criteria before execution, and report any residual coverage gaps.

Risk: Unsupported Playwright invocation patterns or the wrong working directory can produce results that do not represent the intended repository flow.

Mitigation: Use the repository-supported E2E command and the narrowest scope that proves the changed behavior.

Risk: Dedicated local test services can interfere with later checks if they are left running.

Mitigation: Avoid conflicting default ports for dedicated runs and stop dedicated test services after runtime-sensitive validation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown status report with command snippets, pass or failure evidence, prerequisite notes, and residual risk notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the target user flow, module or page scope, any login or seed data, expected success criteria, and repository-supported E2E tooling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
