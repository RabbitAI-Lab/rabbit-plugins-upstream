## Description: <br>
Diagnoses VMware/vSphere/ESXi/NSX incidents by correlating supplied event data into timelines, ranked root-cause hypotheses, and next checks while staying read-only. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and support engineers use this skill to investigate VMware/vSphere incidents from collected events, logs, alarms, and symptoms. It helps build an incident timeline, rank likely causes, and identify the next checks without executing fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ranked hypotheses may be mistaken for a confirmed root cause. <br>
Mitigation: Treat the output as diagnostic guidance; confirm the evidence and run the recommended next checks before any remediation. <br>
Risk: Auth-related investigations may involve local configuration or .env checks. <br>
Mitigation: Limit inspection to the required local configuration and keep any remediation in separate approval-gated tools. <br>
Risk: The skill only correlates events supplied by the calling agent. <br>
Mitigation: Gather real events from the relevant read-only data-source skills and preserve timestamps, sources, and severity values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug) <br>
- [Project homepage](https://github.com/zw008/VMware-Debug) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Unified Event Envelope](references/event-envelope.md) <br>
- [Symptom Routing](references/routing.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, guidance, shell commands, configuration, json] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-compatible diagnostic results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only diagnostic recommendations; CLI output can include JSON event timelines, spikes, hypotheses, and next checks.] <br>

## Skill Version(s): <br>
1.8.7 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
