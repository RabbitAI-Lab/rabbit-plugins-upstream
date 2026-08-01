## Description: <br>
VMware Debug helps agents troubleshoot VMware/vSphere incidents by correlating supplied events into timelines, spikes, ranked root-cause hypotheses, and next checks without making changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to investigate explicit VMware/vSphere/ESXi/NSX incidents by normalizing collected events, correlating them, and deciding which checks or remediation handoff should come next. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package or source could be mistaken for a different publisher because server-resolved GitHub import provenance is unavailable. <br>
Mitigation: Before installing, confirm the vmware-debug package and source are the expected release from publisher handle zw008 and the linked project homepage. <br>
Risk: A ranked hypothesis can be mistaken for a confirmed root cause when the supplied event set is incomplete. <br>
Mitigation: Gather real events from the relevant companion read tools, preserve original timestamps and severity, and present hypotheses as ranked leads until confirmed. <br>
Risk: Full VMware troubleshooting may involve companion skills that access logs, metrics, credentials, or remediation workflows under their own permissions. <br>
Mitigation: Review companion skill permissions separately and route any remediation only through the appropriate confirmation, approval, and audit gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug) <br>
- [Project homepage](https://github.com/vmware-skills/VMware-Debug) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Unified Event Envelope](references/event-envelope.md) <br>
- [Symptom Routing](references/routing.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-compatible MCP or CLI outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only diagnostic outputs; MCP responses include timelines, spikes, ranked hypotheses, and next checks.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
