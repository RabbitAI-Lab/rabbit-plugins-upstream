## Description:

Grafana Cloud (grafana.com). Use this skill for ANY Grafana Cloud request - searching and reading data. Whenever a task involves Grafana Cloud, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Grafana Cloud organization data through an OOMOL-connected account, including billed usage, stack connectivity, available regions, and stack listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes direct remote shell installers that could be risky if run without verification.

Mitigation: Use an official, version-pinned oo CLI installation method with checksum or signature verification before connecting a Grafana Cloud account.

Risk: The skill operates against the connected Grafana Cloud account and may expose organization billing or stack metadata to the agent session.

Mitigation: Use only the intended Grafana Cloud account and connector permissions, and review connector action schemas before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-grafana-cloud)
- [Grafana Cloud Homepage](https://grafana.com/products/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text responses with inline oo CLI commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running actions and to use server-side credential injection.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
