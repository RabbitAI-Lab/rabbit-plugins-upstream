## Description:

Helps operators inspect VMware infrastructure health, inventory, alarms, events, and performance through read-only queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to triage vCenter and ESXi health, investigate VMs, hosts, and datastores, and review alarms and events without changing vSphere resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring requires sensitive vCenter or ESXi credentials.

Mitigation: Use a dedicated read-only VMware account and inject passwords from a secret manager rather than storing them in .env.

Risk: Optional host-log reads, HTTPS MCP access, and Slack or Discord alerts can expose internal hostnames, IPs, usernames, events, or log snippets.

Mitigation: Enable these features only when needed and restrict access to their logs and configured endpoints.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Monitor)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Investigation protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize structured monitoring results and suggest read-only follow-up queries.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
