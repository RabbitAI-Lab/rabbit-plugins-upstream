## Description:

Helps agents research Amazon product opportunities by mining Qinghu keyword data for high-demand, lower-supply search terms, validating demand trends, and tracing keyword traffic to ASINs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, analysts, and commerce operators use this skill to identify keyword-led product opportunities, compare demand against supply, validate trends, and decide which ASINs or product angles merit deeper review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for general keyword-research requests where the user did not intend to use the Amazon/Qinghu workflow.

Mitigation: Confirm that the user wants Amazon keyword research through Qinghu before approving API calls.

Risk: The Qinghu API requires a user-provided token.

Mitigation: Only request or use QINGHU_TOKEN or QHKIT_TOKEN when the user intends to call Qinghu, and avoid exposing the token in outputs.

Risk: External Qinghu API calls may consume Qinghu points.

Mitigation: Follow the skill's pre-call consent flow and report actual point consumption from the response envelope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-picker)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples; may also direct the agent to produce spreadsheet files for larger keyword datasets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include concise conclusions, scoped metrics, trend direction, keyword opportunity tiers, ASIN traffic breakdowns when used, and Qinghu point consumption when paid calls occur.]

## Skill Version(s):

0.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
