## Description:

Runs bounded GameLearningRuntime quality checks against an authorized game or adapter and reports the evidence without treating a passing check as proof of overall game quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Players, developers, and QA engineers use this skill to assess an authorized game, training adapter, replay, or live probe through finite checks and documented evidence. It distinguishes deterministic checks, training metrics, and live acceptance rather than claiming release quality from a single pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QA or training commands may run against an unintended project or exceed the authorized scope.

Mitigation: Confirm the selected project and review each check, training command, and live probe before execution; keep runs bounded.

Risk: Published QA reports may expose proprietary traces, local paths, or secrets.

Mitigation: Review and redact reports before sharing; publish only evidence the project owner authorized.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown findings with dated JSON and self-contained HTML QA reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports separate failures and evidence gaps; checks require an authorized project and bounded scope.]

## Skill Version(s):

0.24.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
