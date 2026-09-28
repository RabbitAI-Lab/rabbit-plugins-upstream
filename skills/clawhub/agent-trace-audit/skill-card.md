## Description:

Builds a traceable timeline of agent actions from a supplied log and highlights writes recorded without a gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and agent operators use this skill to review an action log, reconstruct what an agent did, and identify potentially ungated writes for human follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent action logs may contain sensitive information.

Mitigation: Review the selected log path and contents before granting access; share only logs needed for the audit.

Risk: The declared tool permissions exceed those needed by the included local audit script.

Mitigation: Limit agent permissions to the files and tools required for the specific audit.

Risk: A clean summary does not establish that every ungated write was detected.

Mitigation: Review the underlying log and validate that its action and gate labels match the audit criteria before relying on the findings.

## Reference(s):

- [Agent Trace Audit on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-trace-audit)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text action timeline and violation summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mostly Chinese; findings depend on the supplied action log.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
