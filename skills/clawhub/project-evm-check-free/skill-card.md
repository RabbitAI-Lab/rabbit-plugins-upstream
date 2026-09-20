## Description:

Checks project earned value management worksheets by recalculating CV, SV, CPI, SPI, totals, duplicates, and blanks, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Project managers, finance reviewers, and delivery teams use this skill to check Chinese-language EVM worksheets before monthly progress and cost reporting. It is intended for local arithmetic validation of submitted worksheet data, not for project forecasting or management advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Short trigger terms such as CPI and SPI may activate the skill in broader project-finance conversations.

Mitigation: Use it only when the task is EVM worksheet checking and the input includes recognizable PV, EV, AC, CV, SV, CPI, and SPI columns.

Risk: Documentation mentions anonymous usage statistics, while the security evidence found no implemented network call.

Mitigation: Confirm current release behavior and data-sharing expectations before deployment, especially in restricted environments.

Risk: The free edition intentionally withholds some EVM checks and does not provide project management advice.

Mitigation: Treat the output as arithmetic worksheet validation and review withheld checks before relying on the result for broader project decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-evm-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON containing EVM checks, findings, missing-input messages, and source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the free checks executed and the checks withheld; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.28 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
