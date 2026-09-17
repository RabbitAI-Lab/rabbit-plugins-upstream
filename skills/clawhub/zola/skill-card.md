## Description:

This skill should be used when the user asks about Zola wedding planning data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People planning weddings use this skill to let an agent inspect and manage Zola wedding-planning records, including vendors, budget, guests, seating, inquiries, events, RSVPs, registry items, and gifts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive wedding-planning records, including guests, addresses, RSVPs, budget items, vendors, seating, registry, and gifts.

Mitigation: Install only when the agent is intended to access live Zola wedding data, and limit use to explicit Zola-related requests.

Risk: The tool surface includes add, update, remove, invite, seating, event, vendor, guest, and budget actions that can change live records.

Mitigation: Require user confirmation before adding, updating, removing, inviting, seating, or bulk-changing guests, events, vendors, budget records, or related wedding data.

Risk: Broad activation wording may trigger the skill for general wedding-planning requests that do not require live Zola access.

Mitigation: Prefer explicit Zola-specific requests before invoking tools that read or modify account data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses with optional tool-call guidance and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause the agent to read or change live Zola wedding-planning data through MCP tools.]

## Skill Version(s):

1.12.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
