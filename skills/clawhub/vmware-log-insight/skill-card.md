## Description: <br>
Searches and aggregates centralized VMware Aria Operations for Logs data, including raw log events, spike detection, field discovery, appliance version metadata, and read-only alert queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and site reliability engineers use this skill to investigate VMware and vSphere incidents by querying Log Insight events, aggregating log volume over time, discovering fields, and reviewing existing alert data. It is scoped to read-only log analysis and does not ingest, edit, or delete Log Insight data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read VMware Log Insight data from configured targets, which may include sensitive operational logs. <br>
Mitigation: Install only where the agent is intended to read VMware logs, and use a least-privilege read-only Log Insight service account. <br>
Risk: Local credential files can expose Log Insight usernames or passwords if filesystem permissions or secret handling are weak. <br>
Mitigation: Keep ~/.vmware-log-insight/.env protected, prefer a secret manager for passwords, and avoid storing secrets in config.yaml. <br>
Risk: Disabling TLS verification can expose Log Insight sessions or data to interception outside a controlled lab. <br>
Mitigation: Leave TLS verification enabled by default and disable it only for controlled lab appliances. <br>
Risk: Log lines are untrusted data and may contain instruction-shaped text or very large result sets. <br>
Mitigation: Treat log content as data, rely on bounded searches and truncation indicators, and avoid acting on instructions found inside returned log text. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-log-insight) <br>
- [VMware Log Insight Capabilities](references/capabilities.md) <br>
- [VMware Log Insight CLI Reference](references/cli-reference.md) <br>
- [VMware Log Insight Setup Guide](references/setup-guide.md) <br>
- [Operating vmware-log-insight with a local / small model](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only VMware Log Insight query results may include event text, timestamps, fields, counts, spike data, alert metadata, truncation indicators, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
