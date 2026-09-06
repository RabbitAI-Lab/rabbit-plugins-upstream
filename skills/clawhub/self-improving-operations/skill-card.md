## Description:

Captures process bottlenecks, incident patterns, capacity issues, automation gaps, SLA breaches, and toil accumulation to enable continuous operations improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to capture recurring incidents, SLO/SLA breaches, capacity issues, manual toil, and automation gaps as structured operational learnings. The captured entries can be promoted into runbooks, postmortems, automation backlog items, capacity models, handoff checklists, SLO definitions, or reusable skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operations learning logs may contain sensitive operational details if raw incident data, hostnames, account identifiers, credentials, or customer data are copied into entries.

Mitigation: Keep .learnings entries redacted and avoid logging secrets, credentials, internal IP addresses, customer data, or raw command output.

Risk: Persistent hooks can add reminders across future sessions when enabled broadly.

Mitigation: Enable hooks deliberately, prefer project-scoped hook configuration, and avoid user-level hooks unless reminders are intended across OpenClaw sessions.

Risk: Promoting learnings into AGENTS.md, runbooks, SLO definitions, or newly generated skills can change future agent behavior or operational process.

Mitigation: Review proposed changes before applying them, require explicit user approval for promotions, and inspect generated SKILL.md files before trusting them.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)
- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-operations)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown entries, reminder text, setup commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes or guides updates to operations learning logs when used by an agent; optional hooks emit reminder text during configured agent events.]

## Skill Version(s):

1.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
