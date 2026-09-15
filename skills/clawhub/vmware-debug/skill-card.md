## Description:

Use this skill when troubleshooting VMware, vSphere, ESXi, or NSX incidents: it correlates gathered events into timelines, ranks root-cause hypotheses, suggests next checks, and records diagnostic case evidence without writing to VMware systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to diagnose VMware incidents from pre-collected events, logs, alerts, and case evidence. It helps decide what to inspect next and routes remediation to other VMware skills instead of executing fixes itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents toward VMware credentials, configuration files, sensitive logs, and locally persisted case data.

Mitigation: Review before installing in environments where those materials may be reachable, use a dedicated account, limit filesystem access, and do not allow secret values to be read unless explicitly necessary.

Risk: Submitted case evidence and audit records may contain host names, addresses, log text, and diagnostic conclusions that remain on disk.

Mitigation: Protect or periodically delete ~/.vmware/cases and ~/.vmware/audit.db according to the environment's retention and access-control requirements.

Risk: Runtime package resolution can introduce supply-chain uncertainty for a diagnostic tool used around sensitive infrastructure.

Mitigation: Prefer a verified local install over runtime uvx resolution when possible.

## Reference(s):

- [VMware Debug homepage](https://github.com/vmware-skills/VMware-Debug)
- [agent-guardrails.md](references/agent-guardrails.md)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [event-envelope.md](references/event-envelope.md)
- [routing.md](references/routing.md)
- [setup-guide.md](references/setup-guide.md)
- [VMware-AIops issue 31](https://github.com/vmware-skills/VMware-AIops/issues/31)

## Skill Output:

**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON tool outputs and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostic outputs may include timelines, ranked hypotheses, next checks, case ledger summaries, and local audit references.]

## Skill Version(s):

1.12.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
