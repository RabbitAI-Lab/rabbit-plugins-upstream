## Description:

Trendshift helps agents query current and historical Trendshift and GitHub repository trending data through a user's OOMOL-connected Trendshift account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve latest or historical repository trend rankings, GitHub Trending snapshots, and engagement spike data from Trendshift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote shell installer commands that could execute unverified code.

Mitigation: Review before installing, trust and install the oo CLI separately, and verify installer source and integrity before running curl-to-bash or PowerShell iex commands.

## Reference(s):

- [Trendshift homepage](https://trendshift.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Trendshift skill](https://clawhub.ai/oomol/skills/oo-trendshift)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses server-side credential handling through the user's connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
