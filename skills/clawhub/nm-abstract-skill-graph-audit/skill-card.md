## Description:

Audit Skill() refs; detect hubs, isolates, and dangling targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit Skill(plugin:name) references across a plugin marketplace, identify hubs and orchestrators, and catch dangling or orphaned skill relationships before documentation, renaming, retirement, or release work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger may activate during general discussion of skill audits.

Mitigation: Use the skill only when intentionally analyzing a plugin or skill repository.

Risk: Generated graph recommendations can affect retirement, consolidation, or dangling-reference work.

Mitigation: Review generated reports before acting on dangling-reference or consolidation recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-graph-audit)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide generation of text or JSON graph reports that classify hubs, orchestrators, isolates, and dangling references.]

## Skill Version(s):

1.9.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
