## Description:

Guides when to ask clarifying questions versus proceed autonomously, reducing unnecessary questions when intent is clear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and agent operators use this skill to decide when clarification is necessary and when routine, reversible work can proceed with documented assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may encourage autonomous action when a user expected clarification.

Mitigation: Apply it to routine or reversible work, and ask when ambiguity would materially affect correctness.

Risk: Destructive, security-critical, data migration, breaking change, or production deployment work could be mishandled if confirmation gates are skipped.

Mitigation: Require explicit confirmation for high-stakes or irreversible actions before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-decisive-action)
- [Claude Night Market conserve plugin](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown guidance and decision checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance-only behavior; no external tools, API calls, or credentials are required.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
