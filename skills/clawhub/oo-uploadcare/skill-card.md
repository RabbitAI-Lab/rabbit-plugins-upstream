## Description:

Uploadcare helps agents inspect and manage Uploadcare projects, files, and groups through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to inspect Uploadcare project, file, or group metadata, or perform file lifecycle actions through an OOMOL-connected Uploadcare account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Install the oo CLI manually from a trusted source, verify it where possible, and do not let an agent run curl|bash or irm|iex installer commands automatically.

Risk: The skill can store files permanently or delete Uploadcare files when write or destructive actions are requested.

Mitigation: Require explicit user confirmation of the exact action, target, and payload before any store_file or delete_file command runs.

## Reference(s):

- [ClawHub Uploadcare Skill](https://clawhub.ai/oomol/skills/oo-uploadcare)
- [Uploadcare Homepage](https://uploadcare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are expected as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
