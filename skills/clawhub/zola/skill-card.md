## Description:

This skill helps an agent work with Zola wedding planning data across vendors, budgets, guests, seating, inquiries, events, RSVPs, registry items, gifts, and marketplace discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and manage Zola wedding planning data, including vendors, budget items, guest lists, seating charts, RSVPs, events, registries, gifts, and marketplace discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live add, update, remove, invite, seating, and budget changes to sensitive Zola wedding-planning data.

Mitigation: Use it only for explicit Zola tasks and require user confirmation before executing any write, delete, invitation, seating, or budget-changing action.

Risk: Connecting the skill to a real Zola account exposes sensitive wedding-planning information through account-backed tools.

Mitigation: Review the skill before installation and limit access to users and agents that need to perform Zola wedding-planning tasks.

## Reference(s):


## Skill Output:

**Output Type(s):** [API Calls, Text, Guidance]

**Output Format:** [MCP tool calls and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read, create, update, or delete wedding planning records through Zola API-backed tools.]

## Skill Version(s):

1.12.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
