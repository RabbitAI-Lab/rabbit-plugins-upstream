## Description:

Helps agents use the do CLI to manage tasks, habits, plans, contacts, and other personal life-tracking information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use the do CLI to capture and review tasks, log habits, propose plans, and manage personal contacts and notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can write tasks, plans, contact memories, area settings, and thread messages.

Mitigation: Require explicit user confirmation before allowing an agent to make these changes.

Risk: API keys can grant access to personal data and messaging.

Mitigation: Use the narrowest API key scopes possible and review access before installation.

Risk: Pipe-to-shell installation can run unreviewed setup code.

Mitigation: Prefer a verified package-manager or release install.

## Reference(s):

- [do skill on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [do CLI documentation linked in the skill](https://github.com/robbeverhelst/do)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read personal information or change tasks, plans, contacts, and messages when authorized.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
