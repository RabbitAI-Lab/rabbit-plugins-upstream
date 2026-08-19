## Description:

Provides an agent harness engineering specification for building coding, automation, and long-running agents with loop, provider, tool, permission, session, compaction, prompt and skill, extension, and delivery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edde-101](https://clawhub.ai/user/edde-101)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill as a reference when asking an agent to build a coding, automation, or long-running harness agent. It guides architecture choices, phased implementation, and reusable Python templates without executing code itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable harness templates include broad bash tool access that could execute unsafe commands if copied directly.

Mitigation: Add command allowlisting, workspace sandboxing, path restrictions, and human approval for risky operations before using the templates in an agent.

Risk: Template-based agents may expose sensitive output from shell tools.

Mitigation: Add stronger secret redaction and review tool results before returning them to users or storing them in sessions.

## Reference(s):

- [Server-resolved GitHub import](https://github.com/Edde-101/harness-engineering/tree/main/harness-engineering)
- [ClawHub skill page](https://clawhub.ai/edde-101/skills/harness-engineering-skill)
- [Agent Harness architecture overview](references/architecture.md)
- [Design decision checklist](references/design-decisions.md)
- [Python reference implementation templates](references/code-templates.md)
- [Long-running agent design patterns](references/long-running-patterns.md)
- [Agent harness comparison](references/harness-comparison.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with Python code templates and implementation checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated harness code and shell-command templates should be reviewed before reuse.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter version is 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
