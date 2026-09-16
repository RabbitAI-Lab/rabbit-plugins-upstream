## Description:

InfluxDB Cloud (influxdata.com). Use this skill for ANY InfluxDB Cloud request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate InfluxDB Cloud through an OOMOL-connected oo CLI workflow, including listing and retrieving buckets, querying data with InfluxQL, and writing line protocol data after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly.

Mitigation: Review the oo CLI installation path before installing, prefer an official versioned or checksum-verified installer, and do not let an agent run curl-to-bash or irm-to-iex commands automatically.

Risk: The skill can write line protocol data to InfluxDB Cloud.

Mitigation: Confirm the exact write payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-influxdb-cloud)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [InfluxDB Cloud](https://www.influxdata.com/products/influxdb-cloud/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing write actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
