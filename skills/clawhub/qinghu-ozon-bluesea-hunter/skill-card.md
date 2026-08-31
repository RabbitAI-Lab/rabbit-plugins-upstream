## Description:

This skill helps agents identify under-saturated Ozon Russia category opportunities by drilling into category levels and comparing market, trend, hot-ranking, and brand data from Qinghu APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and analysts use this skill to choose Ozon Russia categories for new stores or product lines. It compares growth, market size, concentration, and brand saturation before recommending 2-3 candidate category lanes and discouraging saturated ones.

### Deployment Geography for Use:

Global (analyzes Ozon Russia marketplace data)

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API key and may consume Qinghu credits during market-data calls.

Mitigation: Require explicit user approval before tool calls, use only user-provided or environment-supplied Qinghu credentials, and report actual Qinghu credit consumption from returned call metadata.

Risk: The skill may export local result files containing category analysis outputs.

Mitigation: Export only data needed for the approved Ozon Russia analysis and provide concise links or previews instead of pasting large datasets into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-bluesea-hunter)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown recommendations with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include category paths, growth comparisons against the market baseline, saturation notes, recommended price or product directions, and concise previews of exported results.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
