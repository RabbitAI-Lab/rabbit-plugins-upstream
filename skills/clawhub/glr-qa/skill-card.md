## Description:

Run goal-driven GameLearningRuntime QA against an authorized game, training adapter, replay, or live probe and produce a dated JSON plus self-contained HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and game project maintainers use this skill to run bounded GameLearningRuntime checks against authorized projects and report concrete evidence about failures, gaps, and training-readiness signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to run local QA, training, replay, or live-probe commands against a game project.

Mitigation: Use it only with authorized projects, review selected checks before execution, and keep each check finite and scoped.

Risk: Generated QA reports can contain proprietary traces, local paths, command output, or other sensitive project evidence.

Mitigation: Publish only owner-authorized evidence and remove secrets, local overrides, and sensitive traces from shared artifacts.

Risk: A passing smoke check or missing live evidence can be misread as full release quality.

Mitigation: Treat missing live evidence as an evidence gap and avoid claiming release quality from this report alone.

## Reference(s):

- [glr-qa ClawHub skill page](https://clawhub.ai/loonghao/skills/glr-qa)
- [loonghao ClawHub publisher profile](https://clawhub.ai/user/loonghao)
- [Package workflow](../glr-cli/references/packages.md)
- [GLR CLI recording contract](../glr-cli/SKILL.md#recording-and-training-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to generated JSON and HTML QA reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect result.json and index.html from a dated .glr-qa output directory.]

## Skill Version(s):

0.19.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
