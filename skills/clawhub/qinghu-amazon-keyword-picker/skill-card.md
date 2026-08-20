## Description:

青虎AI 亚马逊关键词选品 helps agents find Amazon product opportunities by mining buyer search terms for high demand, limited supply, positive trend signals, and non-dominant top results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and agent users use this skill to identify keyword-led product opportunities, validate trend strength, inspect competing ASIN traffic, and produce concise product-selection recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send Qinghu API requests with a token supplied by the user or environment.

Mitigation: Use a scoped Qinghu token where possible, avoid sharing token values in chat, and rotate or revoke the token if exposure is suspected.

Risk: Some Qinghu tools may consume paid credits.

Mitigation: Check the tool's free flag, ask for user approval before paid calls, and report actual Qinghu point consumption when paid calls are made.

Risk: Larger result sets may be written to local spreadsheet or cache files.

Mitigation: Share only the needed export link or summary, and delete local files when they are no longer needed.

Risk: Keyword opportunity metrics and PPC-related values are decision-support estimates rather than guarantees.

Mitigation: Label marketplace, period, and sample scope in outputs, and advise users to validate final launch or ad decisions against their own Amazon and advertising data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-picker)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-RPC request examples and optional spreadsheet file exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Qinghu APIs with a user-provided token; larger result sets may be saved as local spreadsheet or cache files.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
