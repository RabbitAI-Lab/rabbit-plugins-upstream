## Description:

Provides Zola wedding planning support through an MCP server with tools for vendors, budgets, guests, seating, RSVPs, registry items, gifts, and marketplace discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with authorized Zola access use this skill to inspect and manage wedding planning data, including guest lists, budgets, vendors, seating charts, RSVPs, registries, gifts, and vendor inquiries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or modify sensitive wedding planning data, including guest, event, vendor, registry, gift, and budget information.

Mitigation: Invoke it only for explicit Zola tasks with authorized accounts and require confirmation before changing guest lists, addresses, seating, RSVPs, vendors, registry, gifts, or budget data.

Risk: The security summary notes limited scoping and confirmation guidance for actions that affect Zola account data.

Mitigation: Review requested actions before execution and constrain use to the specific Zola account and task the user authorized.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or structured text responses from MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read or modify Zola wedding planning records depending on the selected tool.]

## Skill Version(s):

1.12.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
