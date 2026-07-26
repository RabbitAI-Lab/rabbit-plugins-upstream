## Description: <br>
Grafana Cloud support for reading organization usage, stack connectivity, regions, and stacks through the OOMOL grafana_cloud connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Grafana Cloud organization information through an OOMOL-connected account, including billed usage, stack metadata, stack connectivity, and available regions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can read Grafana Cloud organization information such as billed usage, stack metadata, regions, and connectivity. <br>
Mitigation: Use the skill only when the connected Grafana Cloud account and OOMOL connector access are intended for the requested task. <br>
Risk: First-time setup can install the oo CLI or open account-connection and authentication flows. <br>
Mitigation: Review and approve setup, login, and connection steps before running them; normal actions should not repeat setup unless an auth or connection error occurs. <br>
Risk: Connector schemas may expose write or destructive actions in addition to the read-only actions listed in this artifact. <br>
Mitigation: Require explicit user confirmation of the exact target, payload, and effect before approving any action tagged write or destructive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-grafana-cloud) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Grafana Cloud](https://grafana.com/products/cloud/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
