## Description:

This skill routes Zola wedding planning requests to tools for vendors, budgets, guests, seating, inquiries, events, RSVPs, registry, gifts, and dashboard discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when working with Zola wedding planning data, including guest lists, RSVPs, vendors, budget items, seating, events, registry status, and gift tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests to tools that change live guest, vendor, budget, RSVP, registry, and related wedding planning records.

Mitigation: Confirm user intent before deleting records, bulk-changing invitations, editing budgets, changing addresses, or modifying registry and vendor records.

Risk: The skill operates on Zola account data when connected to the relevant tools.

Mitigation: Install and use it only when the agent is expected to access and act on that Zola account data.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, API Calls, text]

**Output Format:** [Markdown or plain text responses based on Zola account data and tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request or summarize live wedding planning data when connected to a Zola account.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
