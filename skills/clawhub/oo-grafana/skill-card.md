## Description:

Operates Grafana through an OOMOL-connected account to read, create, update, and delete dashboards, folders, data sources, alerts, and contact points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Grafana resources from an agent session through an OOMOL-connected Grafana account. It supports read workflows as well as approved create, update, and delete actions for Grafana resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a pinned or otherwise verifiable release, and do not allow the agent to run remote installer scripts automatically.

Risk: The skill can create, update, or delete Grafana dashboards, folders, and data sources.

Mitigation: Use least-privilege Grafana credentials and require explicit approval before any create, update, or delete action.

Risk: Grafana actions are executed through connected credentials.

Mitigation: Confirm the intended Grafana account, connection state, and permission scope before performing sensitive operations.

## Reference(s):

- [ClawHub Grafana Skill](https://clawhub.ai/oomol/skills/oo-grafana)
- [Grafana Homepage](https://grafana.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses from Grafana actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
