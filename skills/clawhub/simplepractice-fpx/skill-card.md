## Description:

Guides an agent in reading a signed-in SimplePractice Client Portal from the shell to retrieve appointments, billing records, documents, and practice information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Portal users and their authorized agents use this skill to retrieve their SimplePractice appointment, billing, document, and practice information without installing a separate portal server. It covers reading data, not making payments or changing appointments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live portal session cookie can grant access to sensitive health and billing records.

Mitigation: Use a trusted personal machine, restrict the cookie jar to the account owner, keep it out of git and logs, and delete it when finished.

Risk: Portal responses may expose protected health information in shared output or saved files.

Mitigation: Avoid printing or saving health and billing responses in shared locations; review any agent output before sharing.

## Reference(s):

- [SimplePractice FPX release](https://clawhub.ai/chrischall/skills/simplepractice-fpx)
- [SimplePractice Client Portal request reference](references/requests.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell examples and portal response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal guidance; results may contain sensitive health and billing information.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
