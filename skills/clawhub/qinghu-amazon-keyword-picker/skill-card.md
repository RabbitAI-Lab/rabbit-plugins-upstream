## Description:

青虎AI 亚马逊关键词选品 helps agents research Amazon keyword opportunities by mining buyer search terms, checking demand and competition signals, validating trends, and tracing keyword traffic to ASINs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product researchers, and commerce operators use this skill to identify keyword-led product opportunities, compare demand against supply, validate trend durability, and summarize actionable product positioning from Qinghu data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send keyword and product research queries to Qinghu and can use a Qinghu API token from the local environment.

Mitigation: Install and run it only when Qinghu processing is acceptable, provide scoped credentials where possible, and avoid sharing sensitive research terms unless the user has approved that data flow.

Risk: Large keyword datasets may be exported to local spreadsheet files.

Mitigation: Review generated files before sharing them and store or delete exports according to the user's data-handling policy.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-picker)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance, files]

**Output Format:** [Markdown guidance with API request examples and optional spreadsheet exports for larger keyword datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request a Qinghu API token and may export large keyword result sets to local spreadsheet files.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
