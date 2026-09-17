## Description:

PandaDoc helps an agent read, create, update, and delete PandaDoc data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage PandaDoc documents, templates, folders, contacts, attachments, and webhooks through an OOMOL-connected PandaDoc account. The skill supports both read workflows and state-changing workflows that require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup documentation includes remote installer commands for the oo CLI.

Mitigation: Install the CLI only from a trusted, signed, versioned, or checksum-verified source before using the skill.

Risk: Write actions can create or modify PandaDoc documents, templates, folders, contacts, attachments, or webhook subscriptions.

Mitigation: Inspect the live connector schema, review the exact payload and intended effect, and obtain user confirmation before running write actions.

Risk: Destructive actions can delete PandaDoc contacts or templates from the connected workspace.

Mitigation: Confirm the target resource and obtain explicit user approval before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pandadoc)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [PandaDoc Homepage](https://www.pandadoc.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing payloads and to return connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
