## Description:

vmware-debug helps agents diagnose VMware/vSphere/ESXi/NSX incidents by correlating supplied events into timelines, ranking root-cause hypotheses, and suggesting next checks while writing only to a local case ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to investigate explicit VMware/vSphere/ESXi/NSX problems by turning collected logs, events, alerts, and symptoms into a ranked diagnostic timeline and next-check plan. It is for diagnosis and remediation routing, not for executing fixes against VMware systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags credential exposure risk around auth workflows and credential-bearing .env files.

Mitigation: Do not let the agent read raw secret values; redact evidence before submitting it to cases.

Risk: Runtime installation can depend on external package code not present in the reviewed artifact.

Mitigation: Use a preinstalled, verified package where possible, pin the release version, and avoid uvx runtime resolution in sensitive environments.

Risk: Case folders may retain sensitive host names, addresses, log text, and event evidence.

Mitigation: Keep $OPS_HOME access controlled, redact case evidence, and periodically delete old case folders under $OPS_HOME/cases.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project Homepage](https://github.com/vmware-skills/VMware-Debug)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Unified Event Envelope](references/event-envelope.md)
- [Symptom Routing](references/routing.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown/text guidance with JSON MCP or CLI results and shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local case ledger files under $OPS_HOME/cases when case tools are used; stateless correlation returns JSON without writing to VMware systems.]

## Skill Version(s):

1.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
