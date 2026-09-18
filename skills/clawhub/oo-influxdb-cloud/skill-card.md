## Description:

InfluxDB Cloud (influxdata.com). Use this skill for ANY InfluxDB Cloud request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect InfluxDB Cloud connector schemas, list and retrieve Serverless buckets, run InfluxQL queries, and write line protocol data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands executed directly in a shell.

Mitigation: Review the oo CLI installer source and use a verified installation method before running setup commands.

Risk: The write_line_protocol action can change InfluxDB Cloud state.

Mitigation: Use a least-privilege InfluxDB Cloud token and confirm the exact bucket and data before allowing write actions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-influxdb-cloud)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [InfluxDB Cloud](https://www.influxdata.com/products/influxdb-cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing request payloads and to confirm state-changing writes before execution.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
