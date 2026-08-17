## Description:

Operate Grafana through an OOMOL-connected account using the oo CLI to read, create, update, and delete dashboards, folders, data sources, and related alerting resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Grafana resources through an OOMOL-connected account. It is suited for querying Grafana objects and proposing create, update, or delete connector actions when the user has connected Grafana in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Grafana dashboards, folders, or data sources.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

Risk: Destructive actions can remove or overwrite Grafana resources.

Mitigation: Confirm the target identifier and obtain explicit approval before running destructive actions.

Risk: Connector payloads may be malformed if based on stale assumptions.

Mitigation: Inspect the live action schema before building each connector payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-grafana)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Grafana Homepage](https://grafana.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema and connector run commands that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
