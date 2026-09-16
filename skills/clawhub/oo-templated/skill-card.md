## Description:

Templated (templated.io) helps agents read, create, list, retrieve, and delete Templated resources through OOMOL's connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to manage Templated account data, templates, and renders through OOMOL's connected oo CLI workflow. It supports reading templates and renders, creating renders, deleting renders, and handling setup or billing failures when commands require remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts for the oo CLI.

Mitigation: Review the installation path before installing, prefer an official version-pinned installer with checksum or signature verification, and do not let an agent execute the remote install script automatically.

Risk: The skill can create Templated renders and delete existing renders.

Mitigation: Require explicit user confirmation of the payload, target render, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-templated)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Templated Homepage](https://templated.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to inspect live connector schemas before running Templated actions and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
