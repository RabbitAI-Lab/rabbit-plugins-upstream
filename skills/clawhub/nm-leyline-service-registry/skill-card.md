## Description:

Registers external services with health checks, central config, and unified execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and document a registry pattern for coordinating multiple external service integrations with shared configuration, health checks, service selection, failover, and execution result handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured external service CLIs may receive prompts or named files that contain sensitive information.

Mitigation: Use trusted services, review API key setup and service config, and avoid sending sensitive files unless the provider and account policy allow it.

Risk: Broad service and execution triggers may apply external-service registry guidance when the task does not need multi-service coordination.

Mitigation: Confirm the task needs a service registry, shared health checks, or failover behavior before applying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-service-registry)
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Service configuration module](modules/service-config.md)
- [Execution patterns module](modules/execution-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown guidance with Python and YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
