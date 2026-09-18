## Description:

Vimeo (vimeo.com). Use this skill for ANY Vimeo request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Vimeo videos, folders, showcases, tags, metadata, download links, uploads, replacements, and account information through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions pipe remote installer scripts directly into bash or PowerShell without pinning or verification.

Mitigation: Review the installer source first and prefer a trusted, versioned, verified oo CLI installation path before installing.

Risk: Write and destructive Vimeo actions can alter or delete videos, folders, showcases, tags, or metadata.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [ClawHub Vimeo skill page](https://clawhub.ai/oomol/skills/oo-vimeo)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vimeo homepage](https://vimeo.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector JSON output with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
