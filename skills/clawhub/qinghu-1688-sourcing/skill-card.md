## Description:

Guides agents through Qinghu-powered 1688 sourcing workflows, including image-based product matching, keyword sourcing, item detail lookup, supplier comparison, and cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and sourcing teams use this skill to find 1688 suppliers, compare product offers, evaluate supplier fit, and estimate sourcing costs before procurement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound Qinghu API requests using a user-provided token and may transmit product research details.

Mitigation: Use a dedicated Qinghu API key where possible, keep it in approved environment variables, and avoid using sensitive product research in retained or shared environments.

Risk: Qinghu API calls may consume credits after user approval.

Mitigation: Confirm the intended tool calls before the first request, report actual usage from the returned pointCost value, and avoid speculative retries.

Risk: Large sourcing result sets may be exported to local spreadsheet files.

Mitigation: Keep exports scoped to the requested sourcing task, provide the generated file path to the user, and avoid retaining sensitive exports unexpectedly.

Risk: 1688 sourcing matches and supplier data may not prove product quality, authorization, patent status, or fulfillment reliability.

Mitigation: Compare multiple suppliers, state cost assumptions, recommend sample validation, and ask the user to verify brand authorization and patent exposure before procurement.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-1688-sourcing)
- [Qinghu API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Concise Markdown recommendations with supplier comparisons, cost assumptions, risk notes, and spreadsheet exports for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user authorization before Qinghu API calls that may consume credits; larger record sets may be exported as local spreadsheet files.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
