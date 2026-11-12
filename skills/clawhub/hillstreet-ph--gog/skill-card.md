## Description:

Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use this skill to run Google Workspace tasks through the gog command line, including searching and managing Gmail, Calendar, Drive, Contacts, Sheets, and Docs. It also provides OAuth setup and troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth setup and stored credentials can grant access to sensitive Google Workspace data and actions.

Mitigation: Use only the services and scopes needed, keep client secrets, callback URLs, and tokens out of chat, and protect the configured keyring and credential files.

Risk: The security scan inspected one Markdown file and reported partial coverage because two referenced message-file paths were missing.

Mitigation: Treat the benign verdict as incomplete evidence and review the full release contents before deployment.

## Reference(s):

- [gog CLI homepage](https://gogcli.sh)
- [gog on ClawHub](https://clawhub.ai/hillstreet-ph/skills/gog)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
