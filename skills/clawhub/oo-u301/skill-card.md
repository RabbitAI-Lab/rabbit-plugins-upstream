## Description:

U301 helps agents manage U301 short links through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list U301 domains, create short links, and delete existing links through an authenticated OOMOL-connected U301 account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path installs the oo CLI by piping a remote script directly into a shell.

Mitigation: Review the installer or use a verified package or install method before running the remote shell command.

Risk: The skill can create and delete U301 short links in a connected account.

Mitigation: Require explicit user confirmation for exact payloads before write actions and exact targets before destructive actions.

## Reference(s):

- [ClawHub U301 Skill](https://clawhub.ai/oomol/skills/oo-u301)
- [U301 Homepage](https://u301.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before write or destructive U301 actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
