## Description:

AppleDB provides agent access to AppleDB data for searching and reading Apple device and operating system build records through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect AppleDB action schemas, then retrieve or search Apple device and operating system build records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup fallback includes curl-to-bash and PowerShell iex installer commands from an external endpoint.

Mitigation: Use the setup instructions only when the oo CLI is missing, trust the OOMOL installer endpoint before execution, and prefer a pinned, verified install method when available.

## Reference(s):

- [AppleDB homepage](https://appledb.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub AppleDB skill page](https://clawhub.ai/oomol/skills/oo-appledb)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live action schemas before building JSON payloads.]

## Skill Version(s):

1.0.2 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
