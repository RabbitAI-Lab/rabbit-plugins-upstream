## Description:

Jin10 (jin10.com) enables agents to search and read Jin10 market and financial news data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jin10 quotes, K-line data, flash news, news articles, supported quote codes, and the current-week economic calendar through the OOMOL `oo` CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Install the `oo` CLI only from a trusted official path after checking the source, version, and integrity; prefer pinned or package-manager installation methods when available.

Risk: Connector use depends on an authenticated OOMOL account and a connected Jin10 provider.

Mitigation: Run actions only after the user has installed the CLI, signed in, and connected Jin10; use setup or reconnection steps only after an auth or connection error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jin10)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Jin10 homepage](https://www.jin10.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
