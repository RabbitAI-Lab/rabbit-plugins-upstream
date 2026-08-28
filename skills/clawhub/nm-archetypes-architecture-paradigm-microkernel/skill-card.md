## Description:

Applies microkernel architecture with minimal core and plugin extensibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to decide when to apply a microkernel/plugin architecture and to plan core services, plugin contracts, sandboxing, SDKs, and release governance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The guidance may steer design recommendations toward a plugin/microkernel pattern even when the system does not need plugin extensibility.

Mitigation: Review the skill's when-to-use and when-not-to-use criteria before adopting the pattern.

Risk: Architecture guidance alone does not validate implementation security for plugin loading, permissions, or sandboxing.

Mitigation: Run a separate architecture and security review before implementing plugin execution or extension-loading mechanisms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-microkernel)
- [Publisher profile](https://clawhub.ai/user/athola)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown prose with architecture recommendations, adoption steps, deliverables, and risk mitigations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution or local data access; content is architecture reference material.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
