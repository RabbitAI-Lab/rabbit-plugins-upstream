## Description:

Captures staffing-company operations software inquiries, gathers a light problem description, and routes them to a TempGuru contact without promising product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External staffing-company operators use this skill when asking about operations software for scheduling, dispatch, time tracking, or invoicing. The agent confirms the inquiry type, gathers brief company and pain-point context, and routes the user to a TempGuru contact.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: Normal use may collect business contact context such as company name, rough staffing volume, and operational pain points.

Mitigation: Ask only for lightweight routing details and avoid collecting unnecessary sensitive or personal data.

Risk: The optional MCP dependency could be used when it is not needed for a simple operations-software inquiry.

Mitigation: Use no tools for ordinary lead routing; reserve read-only MCP lookups for user-requested event market, role, or benchmark-rate context.

Risk: Operations-software inquiries could be incorrectly routed through the buyer-only request_quote flow.

Mitigation: Route operations inquiries by email, phone, or a user-confirmed draft, and do not use request_quote for this workflow.

Risk: The agent could overstate product features, pricing, availability, or timelines.

Mitigation: State that a TempGuru contact confirms fit and product details, and avoid making product or commercial commitments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-pro-operations)
- [TempGuru AI agent docs](https://tempguru.co/ai-agents)
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt)
- [TempGuru event staffing MCP endpoint](https://mcp.tempguru.co/mcp?source=openai-codex)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text or Markdown with an optional email draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional read-only MCP lookups may provide market, role, or benchmark-rate context; operations inquiries should not be routed through request_quote.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
