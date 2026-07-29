## Description: <br>
InfluxDB Cloud (influxdata.com). Use this skill for InfluxDB Cloud requests that read, create, or update data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and data operators use this skill to inspect InfluxDB Cloud bucket schemas, list or retrieve buckets, run InfluxQL queries, and write line protocol data through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: InfluxDB Cloud queries can expose bucket names, metadata, or database contents visible to the connected API token. <br>
Mitigation: Run read actions only for user-requested scopes and treat query results as sensitive account data. <br>
Risk: The write_line_protocol action changes InfluxDB Cloud state. <br>
Mitigation: Review the exact bucket target, line protocol payload, and intended effect with the user before running the write action. <br>
Risk: First-time CLI installation or account connection steps can grant the agent access to an OOMOL-connected InfluxDB Cloud account. <br>
Mitigation: Perform setup only after an auth or connection failure and only when the user intends to connect InfluxDB Cloud through OOMOL. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-influxdb-cloud) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [InfluxDB Cloud](https://www.influxdata.com/products/influxdb-cloud/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads or connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce read results from InfluxDB Cloud or proposed write payloads that require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.json release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
