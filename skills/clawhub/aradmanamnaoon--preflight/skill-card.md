## Description:

Runs a small verification test before a costly or irreversible operation, estimates the full run's cost as a range, and waits for confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aradmanamnaoon](https://clawhub.ai/user/aradmanamnaoon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to test a small version of an expensive or risky operation, review cost ranges and remaining risks, and decide whether to proceed with the full run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automatic small test may still incur charges or change production data, cloud resources, or shared storage.

Mitigation: Use dry-run, read-only, or sandboxed tests; require explicit approval before a test touches paid services or live resources.

## Reference(s):

- [Preflight on ClawHub](https://clawhub.ai/aradmanamnaoon/skills/preflight)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown preflight report with test results, cost ranges, residual risks, and a confirmation prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the exact cheap-test command, input, outcome, and duration; pauses before the full run.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
