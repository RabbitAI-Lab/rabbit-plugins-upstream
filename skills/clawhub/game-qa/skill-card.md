## Description:

Verifies that a game build launches, renders, responds to input, completes its core loop, reaches a designed outcome, and restarts, using evidence from the tested runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Game developers and QA teams use this skill to verify a playable path through a generated game, record runtime evidence, and report blocking issues and testing limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the project's selected verification command, which may execute project code and write QA evidence files.

Mitigation: Review the verification command before running it and inspect generated evidence and workspace changes.

Risk: Proposed game fixes or test hooks may alter the project beyond the QA report.

Mitigation: Review proposed code changes and test hooks as ordinary workspace edits before accepting them.

## Reference(s):

- [Game QA skill on ClawHub](https://clawhub.ai/worldwonderer/skills/game-qa)
- [QA verification contract](artifact/references/qa-contract.md)
- [Test design method](artifact/references/test-design-method.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON verification report with linked runtime and visual evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Six required checks, a complete-run evidence record, and explicit limitations; results do not establish subjective quality or release readiness.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
