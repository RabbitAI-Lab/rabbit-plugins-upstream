## Description:

Aircall (aircall.io) helps agents search and read Aircall data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Aircall calls, contacts, numbers, teams, and users through an OOMOL-connected Aircall account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands executed directly in a shell.

Mitigation: Install the oo CLI through a verified path and independently trust the installer source before running curl-to-bash or irm-to-iex commands.

Risk: The skill queries Aircall data through a connected OOMOL account.

Mitigation: Use an account and Aircall connection whose permissions match the intended task, and rely on server-side credential injection rather than handling raw Aircall tokens locally.

## Reference(s):

- [Aircall Homepage](https://aircall.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-aircall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from Aircall connector actions when commands are executed.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
