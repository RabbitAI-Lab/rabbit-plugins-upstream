## Description:

An ecommerce carbon and cost analysis skill that uses MCP tools and multi-turn LLM reasoning to calculate shipment weight, cost, and carbon emissions from product, BOM, inventory, warehouse, and logistics data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wedy1106](https://clawhub.ai/user/wedy1106)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operations teams use this skill to answer shipment planning questions that require product search, BOM expansion, item cost and carbon lookup, and logistics cost and emissions calculation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation content and database-derived ecommerce results may be sent to an external AI service without clear disclosure.

Mitigation: Disclose the SiliconFlow endpoint and document what product, inventory, cost, logistics, and conversation data may leave the local environment before using real ecommerce data.

Risk: Backend or database access could expose product, inventory, cost, logistics, or operational data.

Mitigation: Require explicit approval before backend or database access and use only data approved for the analysis context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wedy1106/skills/ecommerce-carbon-analyzer)
- [Publisher profile](https://clawhub.ai/user/wedy1106)
- [SiliconFlow API endpoint](https://api.siliconflow.cn/v1)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Conversational text or Markdown summarizing calculated shipment weight, total cost, and total carbon emissions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call MCP tools repeatedly and may send prompts, conversation context, and tool-derived results to an external LLM endpoint.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
