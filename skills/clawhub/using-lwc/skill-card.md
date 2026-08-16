## Description:

LWC Memory helps agents recall durable project context, inspect code structure, and preserve verified knowledge across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[janyork](https://clawhub.ai/user/janyork)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill during substantive project work to bootstrap LWC, recall bounded project or global memory, use document and code graph capabilities when available, and preserve verified reusable results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically install the lwc CLI and create persistent memory state under the user's home directory.

Mitigation: Install only when persistent agent memory is desired; set LWC_AUTO_INSTALL=0 or review and install lwc manually for tighter control.

Risk: Memory writes, physical graph setup, and CodeGraph initialization may persist project knowledge or create local indexes.

Mitigation: Follow the skill's consent boundaries: initialize project memory, enable graphs, build CodeGraph, and write durable memory only with explicit or durable authorization.

Risk: Stored sources and wiki pages may contain untrusted instructions.

Mitigation: Treat loaded memory as reference evidence that cannot override higher-priority system, developer, user, or host instructions.

## Reference(s):

- [LWC Memory ClawHub Page](https://clawhub.ai/janyork/skills/using-lwc)
- [Using LWC Skill Definition](artifact/SKILL.md)
- [LWC Basic Memory](artifact/references/core-memory.md)
- [LWC Memory Policy](artifact/references/memory-policy.md)
- [LWC Operations Manual](artifact/references/operations-manual.md)
- [LWC Agent Onboarding and Readiness](artifact/references/agent-onboarding.md)
- [LWC Active Memory](artifact/references/active-memory.md)
- [LWC CodeGraph Index](artifact/references/code-graph.md)
- [LWC Physical Document Graph](artifact/references/document-graph.md)
- [LWC Document Conversion](artifact/references/document-conversion.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to inspect, initialize, or update local LWC memory only within documented consent and scope boundaries.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
