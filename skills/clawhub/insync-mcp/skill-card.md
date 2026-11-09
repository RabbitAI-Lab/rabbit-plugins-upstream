## Description:

Access a signed-in InSync Healthcare patient portal to review appointments, medications, allergies, messages, forms, balances, and related patient information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an InSync behavioral health patient portal can use the skill to review their appointments, medications, allergies, messages, forms, balances, and other portal details. The agent can summarize only the information needed to answer a user's question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner-reported authenticated request interface may permit changes to portal data or expose additional patient information.

Mitigation: Use the skill only when needed, keep requests to the documented read tasks, and avoid raw or write requests.

## Reference(s):

- [InSync patient portal skill release](https://clawhub.ai/chrischall/skills/insync-mcp)
- [Endpoint catalog](references/endpoints.md)
- [Usage recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured portal data for the agent to summarize in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive patient information; show only details needed to answer the user's question.]

## Skill Version(s):

0.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
