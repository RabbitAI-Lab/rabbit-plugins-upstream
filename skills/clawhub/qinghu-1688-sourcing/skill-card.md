## Description:

Helps ecommerce sellers find 1688 suppliers using image search, keyword search, and product detail lookup, then compare pricing and supplier fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and sourcing operators use this skill to find matching 1688 products, compare suppliers, estimate procurement costs, and produce supplier recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use Qinghu API keys from QINGHU_TOKEN, QHKIT_TOKEN, or user input.

Mitigation: Confirm the user wants to use the Qinghu service and avoid sharing sourcing data or images that should not be sent to Qinghu.

Risk: Qinghu API calls may spend Qinghu credits.

Mitigation: Request authorization before the first tool call in a session and report actual credit consumption from the returned pointCost value.

Risk: Larger result sets may be exported to local files.

Mitigation: Treat exported sourcing data as local user data and share only the generated file link plus a concise preview.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-1688-sourcing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow API diagnostic endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with supplier comparisons, cost estimates, risk notes, and exported table files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to local export files when result arrays contain 10 or more records.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
