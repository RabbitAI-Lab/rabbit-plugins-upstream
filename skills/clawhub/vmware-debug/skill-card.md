## Description:

vmware-debug helps agents investigate VMware, vSphere, ESXi, and NSX incidents by correlating supplied events, ranking likely root-cause hypotheses, and suggesting next checks without changing VMware systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to troubleshoot VMware incidents from gathered logs, alarms, metrics, and event records. It is suited for diagnosis, evidence tracking, and routing remediation to other tools, not for executing fixes itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires running an external executable package under the user's account.

Mitigation: Install only from a trusted package source and run it in an environment where the user accepts local package execution risk.

Risk: Troubleshooting evidence may include host names, addresses, logs, event text, or secrets if users submit raw sensitive files.

Mitigation: Use a dedicated OPS_HOME, avoid submitting raw .env files or credentials, and review case folders before sharing them.

Risk: Local case folders and audit records can retain sensitive diagnostic data after an investigation closes.

Mitigation: Review ~/.vmware/cases and ~/.vmware/audit.db, and delete stale case folders when retention is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-debug)
- [Project homepage](https://github.com/vmware-skills/VMware-Debug)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Unified event envelope](references/event-envelope.md)
- [Symptom routing](references/routing.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool or CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces diagnostic hypotheses, timelines, next-check guidance, and local case-ledger artifacts; it does not execute remediation.]

## Skill Version(s):

1.13.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
