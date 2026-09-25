## Description:

Provides MCP access to Zola wedding planning data and actions across vendors, budget, guests, seating, inquiries, events, RSVPs, registry, gifts, and discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Zola wedding planning information, including vendors, budget, guests, RSVPs, seating, events, registry items, and gift tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad private wedding planning data, including guest, budget, vendor, event, registry, and gift information.

Mitigation: Install and use it only in trusted environments where the user is comfortable granting access to that Zola account data.

Risk: The skill includes account-changing actions such as adding, updating, removing, inviting, assigning, or booking records without documented scoping safeguards.

Mitigation: Require explicit user confirmation before executing any write, delete, invite, seat assignment, or booking action.

## Reference(s):


## Skill Output:

**Output Type(s):** [API Calls, Structured data, Guidance]

**Output Format:** [Tool calls and structured MCP responses summarized as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private wedding planning data and account-changing actions.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
