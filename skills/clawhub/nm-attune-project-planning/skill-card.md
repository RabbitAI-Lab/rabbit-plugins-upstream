## Description:

Converts a completed specification into a phased, dependency-ordered implementation plan before execution begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill after specification work to plan architecture, task breakdowns, dependencies, acceptance criteria, estimates, risks, and sprint sequencing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The planning workflow may immediately proceed into implementation after saving docs/implementation-plan.md.

Mitigation: Use `--standalone` or explicitly tell the agent to stop after planning, then review the implementation plan before allowing execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-planning)
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration, Shell commands]

**Output Format:** [Markdown with structured task plans and inline command or skill-invocation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update docs/implementation-plan.md and may continue into an execution phase unless bypassed.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
