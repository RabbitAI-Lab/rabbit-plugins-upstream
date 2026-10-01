## Description:

Helps agents search, read, compose, send, forward, and organize Gmail messages and drafts through AgentPMT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to automate Gmail searches, customer follow-ups, notifications, inbox organization, and draft review through a connected AgentPMT account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to sensitive email through a third-party service.

Mitigation: Review before connecting a sensitive mailbox and use only an AgentPMT account you trust.

Risk: Messages may be sent, replied to, or forwarded without clear confirmation gates.

Mitigation: Confirm recipients and content with the user before sending or forwarding, including draft sends.

Risk: Trashing messages or deleting drafts may remove important mail.

Mitigation: Require clear user approval before trashing messages or deleting drafts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/agentpmt/skills/gmail-all-email-actions)
- [AgentPMT Gmail marketplace listing](https://www.agentpmt.com/marketplace/gmail-all-email-actions)
- [AgentPMT account and API setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [Gmail action schema](artifact/schema.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Email text or HTML and structured Gmail action requests and results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include attachments, message metadata, and draft content.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
