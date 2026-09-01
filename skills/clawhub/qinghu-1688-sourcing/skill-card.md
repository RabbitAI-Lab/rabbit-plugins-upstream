## Description:

Helps ecommerce sellers source 1688 products through image search, keyword search, product-detail lookup, supplier comparison, and purchasing-cost assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and sourcing agents use this skill to find matching 1688 suppliers, compare prices and minimum order quantities, inspect supplier details, and estimate sourcing risk before purchasing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API key to call 1688 sourcing tools.

Mitigation: Use a scoped Qinghu token where possible and keep unrelated secrets out of accessible environment variables.

Risk: Some Qinghu tool calls may consume points.

Mitigation: Confirm point-cost use before calls and report actual consumption from returned point-cost values.

Risk: Large sourcing results may be exported to local files.

Mitigation: Review exported files before sharing and keep them in an appropriate local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-1688-sourcing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with comparison tables, concise recommendations, API-call examples, and file links for larger exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export larger result sets to local spreadsheet files when records exceed chat-friendly size.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
