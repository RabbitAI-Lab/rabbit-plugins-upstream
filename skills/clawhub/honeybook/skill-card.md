## Description:

Helps users review HoneyBook client-portal projects, contracts, invoices, messages, meetings, and tasks, and prepare portal actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients use this skill to check vendor projects, documents, payments, and communications, and to request links or confirmed messages for follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Locally cached HoneyBook sessions could expose access to client portals.

Mitigation: Protect the local device and session files, and use only portal links from trusted vendor communications.

Risk: Client and vendor records may contain sensitive personal or payment information.

Mitigation: Limit access and sharing to information needed for the user's request.

Risk: Messages can reach vendors and co-clients; signing and payment links can lead to consequential actions.

Mitigation: Review recipients and content before approving a send, and check contract and payment details in the portal before acting.

## Reference(s):

- [Honeybook skill release](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Portal links]

**Output Format:** [Markdown with portal links when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can summarize portal records and provide signing or payment links; sending messages requires user confirmation.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
