## Description:

Social Fetch helps agents search and read Social Fetch data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Social Fetch account details, credit balance, and public social profiles or channels by handle through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly in a shell.

Mitigation: Review the installer source and prefer a pinned, verified installation method before running curl-to-bash or Invoke-Expression commands.

Risk: Commands operate through a connected OOMOL account and can access Social Fetch account, balance, and public profile data.

Mitigation: Fetch the live action schema before each request, send only the required payload, and require explicit confirmation before any future write or destructive action is used.

## Reference(s):

- [Social Fetch homepage](https://www.socialfetch.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-social-fetch)
- [Social Fetch icon](https://static.oomol.com/logo/third-party/social_fetch.svg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
