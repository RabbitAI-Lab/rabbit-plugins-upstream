## Description:

Bugsnag connector for searching and reading Bugsnag organizations, projects, errors, events, and releases through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to inspect Bugsnag organizations, projects, errors, events, and releases from an OOMOL-connected Bugsnag account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remotely fetched shell and PowerShell installers.

Mitigation: Review the installer source before execution and prefer a verified package, pinned release, checksum or signature verification, and non-admin execution.

Risk: Bugsnag credentials are managed through an OOMOL-connected account.

Mitigation: Confirm the account owner accepts OOMOL server-side credential management before connecting Bugsnag.

## Reference(s):

- [ClawHub Bugsnag Skill](https://clawhub.ai/oomol/skills/oo-bugsnag)
- [Bugsnag Homepage](https://www.bugsnag.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON data from Bugsnag connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
