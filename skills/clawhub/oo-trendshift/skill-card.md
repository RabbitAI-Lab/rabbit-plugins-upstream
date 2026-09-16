## Description:

Trendshift lets agents retrieve current and historical repository trending rankings and GitHub Trending snapshots through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and external users use this skill to query Trendshift rankings, GitHub Trending snapshots, and repository engagement spikes from an OOMOL-connected Trendshift account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup uses remote installer scripts for the oo CLI.

Mitigation: Review setup commands before installation, prefer signed or checksum-verified installers, and avoid running remote scripts from an elevated shell.

Risk: Authentication and connection setup can change local login state and external OOMOL account state.

Mitigation: Run login or connection steps only after an auth or connection failure and confirm the account and Trendshift connection before retrying.

## Reference(s):

- [Trendshift homepage](https://trendshift.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trendshift)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector JSON responses when actions are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
