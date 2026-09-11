## Description:

This skill lets an agent help manage Zola wedding planning data, including vendors, guests, budgets, seating, RSVPs, registry items, gifts, and marketplace discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning a wedding can use this skill to ask an agent to inspect and update Zola planning data across vendors, budgets, guests, events, seating, registry items, gifts, and inquiries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose private wedding planning data, including guest addresses, RSVP status, gifts, budget details, and vendor conversations.

Mitigation: Install only when the agent is expected to access this Zola account data, and treat returned guest, registry, gift, budget, and vendor information as private.

Risk: The skill includes write-capable actions that can change vendors, guests, addresses, events, seating assignments, invitations, and budget items.

Mitigation: Before allowing write actions, confirm the exact account, event, guest, vendor, seat, invitation, or budget item involved.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text summaries, confirmations, and guidance based on Zola MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive wedding account data such as guest addresses, RSVPs, gift records, vendor conversations, budget items, and account changes.]

## Skill Version(s):

1.12.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
