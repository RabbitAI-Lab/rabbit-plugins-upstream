## Description:

Transforms unstructured weekly work notes into a leadership-focused weekly report using a four-step workflow that builds project context, organizes facts, asks for missing risk/plan/insight details, and assembles a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT

## Use Case:

Employees, freelancers, and managers use this skill to turn informal weekly status notes into concise reports for leadership review. It is intended for weekly reports, monthly reports, work updates, meeting materials, and upward management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Weekly reports may contain sensitive project names, customer details, risks, and internal status notes.

Mitigation: Confirm that the information is appropriate to share with the AI client before using the skill.

Risk: Fields marked as inferred may be incorrect or unsupported by confirmed facts.

Mitigation: Review and replace any inferred content before sending the report.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/handsomeng/skills/hs-weekly-report)
- [Prompt template](references/prompt-template.md)
- [Workflow example](references/example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown weekly report with structured sections and follow-up questions when required information is missing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided project context and work status details; any inferred fields should be reviewed before sending.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
