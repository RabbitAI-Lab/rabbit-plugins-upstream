## Description:

Applies microkernel architecture with minimal core and plugin extensibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to decide when a microkernel/plugin architecture fits a system and to plan core services, plugin contracts, sandboxing, SDK support, and release governance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad architecture triggers may surface this skill in general architecture or plugin discussions where more specific guidance is preferable.

Mitigation: Confirm the system actually needs microkernel or plugin extensibility before applying the recommendations.

Risk: Plugin-based systems can accumulate unmanaged extensions, version skew, or core bloat.

Mitigation: Use the skill's recommended plugin contracts, compatibility matrix, sandboxing model, and review process to keep extensions governed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-archetypes-architecture-paradigm-microkernel)
- [Claude Night Market archetypes](https://github.com/athola/claude-night-market/tree/master/plugins/archetypes)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown text with architecture recommendations and deliverable lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; no executable behavior or privileged access is identified in security evidence.]

## Skill Version(s):

1.9.18 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
