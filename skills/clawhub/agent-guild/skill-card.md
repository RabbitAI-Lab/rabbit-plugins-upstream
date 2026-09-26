## Description:

Agent Guild is a local-first cross-agent shared memory protocol that lets multiple AI agents on a user's devices share identity, rules, memory, focus, logs, skills, and handoff messages through local Markdown and JSON files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Agent Guild to connect local AI agents to a shared on-device memory and handoff directory so identity, rules, project state, logs, and skills can persist across sessions and devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared writable rules and shared skills can affect every connected local agent.

Mitigation: Install only when cross-agent memory sharing is intended, and review ~/.agent-guild/rules/ and ~/.agent-guild/skills/ regularly.

Risk: Automatic upgrade apply mode can replace the shared skill used by multiple agents.

Mitigation: Prefer reviewed or manual upgrade steps, and enable automatic apply mode only for trusted release channels.

Risk: Pipe-to-shell installer flows can execute remote code before review.

Mitigation: Prefer reviewed manual installation steps when evaluating or deploying the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dqsjqian/skills/agent-guild)
- [Agent Guild Repository](https://github.com/dqsjqian/agent-guild)
- [Runtime Skill Definition](SKILL.md)
- [Capabilities Reference](references/CAPABILITIES.md)
- [Onboarding Guide](references/ONBOARDING.md)
- [Agent Guild Specification](references/SPEC.md)
- [Security and Capability Disclosure](references/SECURITY.md)
- [Portability Guide](references/PORTABILITY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and local file path conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local operational guidance and CLI commands for shared on-device agent memory; no API response schema.]

## Skill Version(s):

3.10.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
