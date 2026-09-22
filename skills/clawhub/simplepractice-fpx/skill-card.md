## Description:

Read SimplePractice Client Portal data from a shell with curl, including appointments, billing documents, documents to sign, announcements, and practice or clinician information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to script read-only access to their own SimplePractice Client Portal data without running the SimplePractice MCP server. It helps an agent produce curl commands, JSON:API request guidance, and parsing examples for portal reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps an agent use a live SimplePractice session cookie to read portal data that may include protected health information.

Mitigation: Treat the cookie file like a password: keep it chmod 600, out of git, and off shared machines.

Risk: An authenticated portal session could expose sensitive appointments, billing records, documents, announcements, and clinician or practice details.

Mitigation: Use the skill only for your own portal data and review command outputs before sharing or storing them.

Risk: Portal writes such as signing documents, payments, and cancellations carry user-impacting consequences.

Mitigation: Use the SimplePractice portal itself for signing, payments, cancellations, or other writes; keep this skill to read-oriented workflows.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal access guidance; uses a local cookie jar and practice-specific host configuration.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
