## Description:

Dropbox Sign (sign.dropbox.com). Use this skill for Dropbox Sign requests that search and read account, signature request, and template data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to retrieve Dropbox Sign account settings, signature requests, and templates through the oo CLI using an OOMOL-connected Dropbox Sign account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet installer commands executed directly in a shell.

Mitigation: Use a pinned, checksummed, or package-manager installation path for the oo CLI, and independently verify the installer source before running any pipe-to-shell command.

Risk: Future Dropbox Sign connector actions may change account state even though the documented actions are read-oriented.

Mitigation: Inspect the live action schema and confirm the exact payload and user intent before running any action marked write or destructive.

## Reference(s):

- [Dropbox Sign ClawHub Skill](https://clawhub.ai/oomol/skills/oo-dropbox-sign)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Dropbox Sign Homepage](https://sign.dropbox.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; action responses are returned as JSON with data and metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
