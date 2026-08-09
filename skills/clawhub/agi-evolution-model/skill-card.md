## Description:

AGI数字伙伴 is a conversational digital companion skill that uses a dual-loop AGI evolution model with intentionality analysis, personality mapping, metacognitive checks, error-wisdom memory, and five-dimensional intelligence tagging to support dialogue, personality customization, complex problem solving, and learning from errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to add a persistent digital companion workflow for conversation, personality customization, memory-backed reflection, metacognitive checks, error prevention, and dimension-tagged reasoning. It is intended for broad interactive assistance where local workspace access and retained history are explicitly acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can provide a conversational companion with broad local command, file, process, background activity, and stored-history capabilities.

Mitigation: Install and run it only in a constrained workspace or sandbox, and enable CLI execution, file operations, process management, daemons, and archival memory only when they are needed and explicitly accepted.

Risk: Stored interaction history may retain sensitive or long-lived user context.

Mitigation: Use a dedicated memory directory, review retention needs before deployment, and clear or isolate stored history when handling sensitive work.

## Reference(s):

- [AGI数字伙伴 ClawHub listing](https://clawhub.ai/kiwifruit13/skills/agi-evolution-model)
- [Architecture](references/architecture.md)
- [Capability Boundaries](references/capability_boundaries.md)
- [Intelligence Agent Response Rules](references/intelligence-agent-response-rules.md)
- [CLI Tools Guide](references/cli-tools-guide.md)
- [Usage Examples](references/usage-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory files under the configured memory directory when supporting scripts are used.]

## Skill Version(s):

1.0.3 (source: server release metadata, created 2026-08-07T11:36:01Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
