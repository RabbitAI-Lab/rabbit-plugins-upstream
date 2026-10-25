## Description:

Retrieve the user's personal memories saved by Looki, including moments, life summaries, chat history, health reports, and journals through an authorized Looki connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[looki](https://clawhub.ai/user/looki)

### License/Terms of Use:

MIT-0

## Use Case:

People with authorized access to their Looki account use this skill to recall daily activities, life and chat summaries, health reports, and saved journals while keeping responses relevant to their question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal memories may expose private health, location, chat, or media details to an unintended audience.

Mitigation: Confirm the authenticated account and requester's authorization; retrieve only necessary dates and records, and omit unrelated private details.

Risk: Installing or authenticating an access method could change the user's environment or expose account access.

Mitigation: Request separate approval before CLI installation or login, and do not expose credentials or authorization links.

Risk: Incomplete query results may be mistaken for a complete personal history.

Mitigation: Check pagination and requested date coverage, and label incomplete answers as partial.

## Reference(s):

- [Looki Personal Memory skill listing](https://clawhub.ai/looki/skills/looki-personal-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are scoped to accessible records and identify incomplete coverage.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
