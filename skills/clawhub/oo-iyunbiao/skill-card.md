## Description:

Yunbiao is a connector skill for reading, creating, updating, uploading, downloading, and querying Yunbiao data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to work with Yunbiao forms, users, roles, templates, attachments, enterprise cloud files, and data interfaces through an OOMOL-connected account. It supports read workflows and state-changing operations that require schema inspection and user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask users to run a remote oo CLI installer before use.

Mitigation: Install only if you trust OOMOL's installer distribution, and inspect or verify the installer before running it.

Risk: The connected account can access Yunbiao data through the configured connector.

Mitigation: Use an appropriate Yunbiao account for the task and proceed only when granting that access is acceptable.

Risk: Write-capable actions can create, update, upload, or trigger Yunbiao business logic.

Mitigation: Inspect the live action schema and require explicit confirmation of the payload and expected effect before running state-changing actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-iyunbiao)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Yunbiao Homepage](https://www.iyunbiao.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads; state-changing actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
