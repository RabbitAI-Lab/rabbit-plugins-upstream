## Description:

vmware-debug helps agents troubleshoot VMware, vSphere, ESXi, and NSX incidents by correlating supplied events, ranking root-cause hypotheses, and recommending the next checks without applying fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to investigate active VMware or vSphere problems, correlate event evidence from companion skills, and decide what data to collect or which remediation path to route to next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as read-only, but security evidence notes persistent local case-writing behavior under ~/.vmware/cases/ and possible audit logging under ~/.vmware/audit.db.

Mitigation: Review local storage, retention, and cleanup behavior before installation, and treat recorded case data as sensitive operational data.

Risk: Root-cause hypotheses can be incomplete or misleading when the agent supplies sparse, single-source, or poorly normalized events.

Mitigation: Gather evidence from multiple relevant VMware data-source skills, preserve timestamps and event_type fields, and treat next checks as investigation steps rather than confirmed findings.

Risk: The skill routes remediation recommendations to executor skills, which may be inappropriate if a fix is ambiguous or high impact.

Mitigation: Require operator review before handing fixes to vmware-aiops or vmware-pilot, and use their confirmation, approval, rollback, and audit controls for execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Metadata Homepage](https://github.com/vmware-skills/VMware-Debug)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Unified Event Envelope](references/event-envelope.md)
- [Symptom Routing](references/routing.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce ranked hypotheses, timelines, next-check guidance, CLI commands, MCP configuration snippets, and local case records.]

## Skill Version(s):

1.11.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
