## Description:

Provides agent guidance for operating PandaDoc through an OOMOL-connected account, including reading, creating, updating, and deleting PandaDoc documents, templates, folders, contacts, attachments, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected PandaDoc workspace from an agent, including listing and retrieving records and preparing create, update, webhook, and deletion actions with appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute arbitrary code during first-time setup.

Mitigation: Prefer a verified, pinned installer or manual oo CLI installation, and review installer contents before execution.

Risk: Write, destructive, and webhook actions can change or remove PandaDoc workspace data.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval before destructive actions or webhook creation.

Risk: Connector schemas, credentials, scopes, and billing status can differ from static skill text.

Mitigation: Inspect the live action schema before constructing payloads and use the first-time setup guidance only after matching auth, connection, scope, or billing errors.

## Reference(s):

- [PandaDoc homepage](https://www.pandadoc.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pandadoc)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; connector action responses can be returned as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
