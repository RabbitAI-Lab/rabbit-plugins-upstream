## Description:

Reads a user's InSync Healthcare patient portal for appointments, medications, allergies, messages, pending forms, balances, and account counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

An assistant uses this skill to help a patient review relevant information from their InSync portal, such as appointments, medications, messages, forms, allergies, or balances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw requests can invoke account-changing endpoints and expose sensitive portal responses without filtering; opening an unread message may mark it read.

Mitigation: Prefer a version restricted to reviewed read operations with sensitive responses filtered. Obtain user consent before opening unread messages, and share only information needed for the question.

## Reference(s):

- [InSync portal endpoint catalog](references/endpoints.md)
- [InSync usage recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/insync-mcp)

## Skill Output:

**Output Type(s):** [JSON, Health information]

**Output Format:** [Projected JSON that can be summarized in concise text for the user's question.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive patient and account information; show only what is needed for the user's question.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
