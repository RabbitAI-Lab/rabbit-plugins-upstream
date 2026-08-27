## Description:

Tracks per-agent token usage and flags waste in parallel dispatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill after parallel agent runs to review token spend, duplicate work, coordination overhead, and other waste signals before deciding whether future dispatches should use fewer or more focused agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be used with broad agent logs or token-history data that include private workflow details.

Mitigation: Use bounded, intentional workflow data and avoid broad private logs unless that is the intended review scope.

Risk: Waste classifications can incorrectly discourage useful parallel review if interpreted without task context.

Mitigation: Treat the waste signals as post-dispatch review guidance and confirm findings against the actual agent outputs before changing dispatch practices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-agent-expenditure)
- [Conserve plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [guidance, markdown, analysis]

**Output Format:** [Markdown guidance and review checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; documentation-only guidance for post-dispatch review.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
