## Description:

Provides Zola wedding planning support through MCP tools for vendors, budgets, guests, seating, inquiries, events, RSVPs, registry, and gifts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer explicit Zola wedding planning requests and to manage wedding vendors, budget items, guests, seating, inquiries, events, RSVPs, registry items, and gift tracking through available Zola MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Zola wedding planning data may be exposed through broad read access.

Mitigation: Use the skill only for explicit Zola requests and review outputs before sharing personal wedding, guest, vendor, registry, or budget details.

Risk: Write-capable tools can add, update, remove, invite, or bulk-change guests, vendors, events, budgets, seating, registry, or gift-tracker records.

Mitigation: Require confirmation before any mutating or bulk operation against a real Zola account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola-mcp)

## Skill Output:

**Output Type(s):** [Text, API calls, Guidance]

**Output Format:** [Markdown or plain text responses with MCP tool calls where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and modify Zola wedding planning records when connected to a real Zola account.]

## Skill Version(s):

1.7.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
