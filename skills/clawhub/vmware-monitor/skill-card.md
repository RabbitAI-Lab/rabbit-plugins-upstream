## Description:

vmware-monitor helps agents perform safe, read-only VMware vCenter and ESXi monitoring across inventory, alarms, events, performance, capacity, snapshots, and object investigations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators, administrators, and support engineers use this skill to ask an agent for read-only VMware vCenter and ESXi health, inventory, alarm, event, performance, capacity, snapshot, and investigation summaries before taking action in other tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles VMware infrastructure credentials and operational data.

Mitigation: Use a dedicated VMware account with the built-in Read-Only role and inject passwords from a secret manager instead of storing them in .env.

Risk: Webhook alerts can disclose operational details such as hostnames, IP addresses, usernames, event text, and log snippets.

Mitigation: Enable Slack or Discord webhooks only for destinations the operator controls, and treat those destinations as receiving operational data.

Risk: Additional VMware privileges for session listing or host log access can exceed the baseline read-only role.

Mitigation: Grant privileges such as session listing or host log access only when those specific reads are needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Read-only enforcement test](https://github.com/vmware-skills/VMware-Monitor/blob/main/tests/eval/regression/test_read_only_enforcement.py)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Cluster Health Summary Display Template](references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with CLI commands, structured tool-result summaries, and optional local HTML snapshot guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is read-only toward vSphere; some outputs may summarize sensitive operational data such as hostnames, IP addresses, usernames, events, alarms, and log snippets.]

## Skill Version(s):

1.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
