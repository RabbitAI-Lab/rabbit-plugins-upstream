## Description:

Helps creators write, optimize, publish, and manage AI-Shifu courses and review their learner analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators use this skill to develop MarkdownFlow lessons and course prompts, manage publication on AI-Shifu, and examine course and learner performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable login tokens are stored in the user's configuration directory.

Mitigation: Protect local account access and review where credentials are stored before enabling platform operations.

Risk: Course imports, publication, archives, and local edits can change existing content.

Mitigation: Review proposed changes and confirm consequential platform actions before proceeding.

Risk: Learner-level analytics may expose sensitive personal information.

Mitigation: Limit queries and sharing to information needed for the authorized course task.

## Reference(s):

- [AI-Shifu Course Creator release](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Course authoring workflow](references/orchestration-workflow.md)
- [Publishing workflow](references/deployment-workflow.md)
- [Analytics overview](references/analytics/overview.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown and MarkdownFlow course content, with operational guidance and commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or edit local course files and, with confirmation, manage platform courses and query analytics.]

## Skill Version(s):

1.2.12 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
