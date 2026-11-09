## Description:

Diagnoses VMware, vSphere, ESXi, and NSX incidents by correlating evidence, ranking root-cause hypotheses, and recommending next checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware administrators use this skill to investigate incidents from collected logs, alarms, and events. It builds timelines, ranks possible causes, records investigation evidence locally, and recommends the next check or remediation handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial: three local path-like references could not be matched to bundled files, despite a benign verdict with medium confidence.

Mitigation: Review the unresolved references and account for this evidence gap before installing.

Risk: Local case records can contain host names, addresses, and event or log text, and case files have no automatic retention limit. The audit trail stores call metadata and redacts selected payload fields.

Mitigation: Restrict access to case and audit data, and remove case folders when their records are no longer needed.

Risk: Optional HTTPS makes the MCP server reachable over a network and relies on caller bearer tokens and TLS files.

Mitigation: Protect tokens and TLS files as secrets, and expose the endpoint only to intended callers.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage](https://github.com/vmware-skills/VMware-Debug)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Event envelope](references/event-envelope.md)
- [Symptom routing reference](references/routing.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Incident timelines, ranked hypotheses, next-check recommendations, and case records in Markdown and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Correlates caller-supplied event data; case records are stored locally.]

## Skill Version(s):

2.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
