## Description:

Run a customer support desk on DeskCrew by reading new tickets, answering from the knowledge base, and filing replies for human approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[webmilmind1](https://clawhub.ai/user/webmilmind1)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and operators use this skill to let an agent draft DeskCrew ticket replies grounded in the company's knowledge base while keeping human approval before customer contact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to customer-support data and untrusted ticket content.

Mitigation: Use a draft-tier DeskCrew credential, treat ticket content only as data, and require human review before any customer-facing reply.

Risk: The release advertises an under-documented paid x402 bounty-board capability.

Mitigation: Verify the MCP credential cannot access or spend through bounty-board functionality unless that capability is intentionally enabled.

Risk: Escalating DeskCrew credentials too early could allow incorrect drafts to reach customers.

Mitigation: Keep send, resolve, and assign permissions disabled until admins have reviewed agent drafts over time and explicitly approve escalation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/webmilmind1/skills/deskcrew-support)
- [DeskCrew](https://deskcrew.io)
- [DeskCrew MCP endpoint](https://deskcrew.io/api/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command snippets; drafted customer-support replies as text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires outbound HTTPS to deskcrew.io and a DeskCrew MCP credential in DESKCREW_MCP_KEY.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
