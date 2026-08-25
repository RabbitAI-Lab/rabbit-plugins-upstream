## Description:

青虎AI 亚马逊爆款趋势挖掘 helps agents find current Amazon best sellers and rising product opportunities by filtering sales, revenue, BSR growth, ratings, review count, margin, seller structure, and history-backed trend signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to conduct Qinghu-backed Amazon product research, including finding best sellers, identifying rising opportunities, scanning categories, checking ASIN trends, and summarizing product-level risks before selection decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for product-research calls.

Mitigation: Use short-lived or appropriately scoped credentials where possible, prefer environment variables over pasting long-lived keys, and avoid sharing tokens beyond the active task.

Risk: Qinghu-backed calls may consume credits after the session authorization step.

Mitigation: Confirm the intended tools before the first call, report actual credit usage from the Qinghu response envelope, and stop when authorization or cost expectations are unclear.

Risk: Large result sets may be exported to local spreadsheet files and reused by path.

Mitigation: Tell users when a file is created, reference the file path instead of copying large datasets into chat, and handle exported product data according to the user's data-retention expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-trend-hunter)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON API request examples and optional spreadsheet exports for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include product opportunity judgments, supporting metrics, risk notes, and Qinghu credit usage when paid calls are made.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
