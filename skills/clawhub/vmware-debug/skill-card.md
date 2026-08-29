## Description:

VMware Debug helps agents troubleshoot VMware/vSphere incidents by correlating supplied event and log data into timelines, ranked hypotheses, and next checks while remaining read-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to investigate VMware, vSphere, ESXi, or NSX incidents from supplied logs, alarms, and events. It ranks likely causes and recommends follow-up checks while routing any actual remediation to separate gated tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes event and log data supplied by the user or gathered through companion skills, which may contain sensitive infrastructure details.

Mitigation: Install only if comfortable with a community VMware troubleshooting package handling that data; redact or limit event inputs when needed.

Risk: Ranked hypotheses and next checks can be mistaken for confirmed root cause or execution approval.

Mitigation: Treat the output as diagnostic guidance, verify against the supplied evidence, and route remediation only through the separate gated aiops or pilot tools.

Risk: Family tooling may record local audit entries under ~/.vmware/audit.db.

Mitigation: Account for local audit records in operational and privacy review before using the VMware skill family.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage](https://github.com/vmware-skills/VMware-Debug)
- [Capabilities](artifact/references/capabilities.md)
- [Unified Event Envelope](artifact/references/event-envelope.md)
- [Symptom to Signal Routing](artifact/references/routing.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [JSON tool responses and concise Markdown or text diagnostic summaries with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only offline correlation over supplied event data; outputs include timelines, spike summaries, ranked hypotheses, and next checks.]

## Skill Version(s):

1.8.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
