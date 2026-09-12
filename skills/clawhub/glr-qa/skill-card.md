## Description:

Run goal-driven GameLearningRuntime QA against an authorized game, training adapter, replay, or live probe and produce a dated JSON plus self-contained HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to run bounded GameLearningRuntime checks against authorized game projects, training adapters, replays, or live probes. It helps turn a plain-language QA objective into inspectable JSON and HTML evidence while preserving evidence boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose running local QA commands against a project, adapter, replay, or live probe outside the user's authorized scope.

Mitigation: Confirm the authorized project, adapter, and evidence scope before running commands, and keep every check finite and bounded.

Risk: Generated JSON or HTML reports may include proprietary traces, local paths, command output, or secrets if shared without review.

Mitigation: Review generated reports before publication and share only evidence the project owner authorized.

Risk: A passing smoke command or bounded QA run may be mistaken for complete release quality proof.

Mitigation: Report QA results as scoped evidence and clearly identify missing live evidence or broader release-validation gaps.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to generated JSON and HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish deterministic checks, replay, training metrics, and live-host evidence; reports should omit proprietary traces, local paths, and secrets unless authorized.]

## Skill Version(s):

0.15.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
