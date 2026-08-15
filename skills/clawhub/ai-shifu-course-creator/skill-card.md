## Description:

Helps AI-Shifu course authors create, edit, optimize, deploy, publish, manage, and analyze MarkdownFlow-based Teaching Prompts and Course Prompts across the course lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course authors, operators, and administrators use this skill to turn source material into AI-Shifu courses, revise existing courses, publish live course updates, and review learner, revenue, credit, and engagement analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated course-management commands can publish, modify, reorder, archive, or otherwise affect live AI-Shifu courses.

Mitigation: Review target course identifiers, generated import files, and publish steps before platform mutations; use the local or artifact-only route when platform changes are not intended.

Risk: Analytics workflows can query learner progress, revenue, ratings, credit use, and learner-linked records.

Mitigation: Use the documented privacy presentation rules, avoid exposing raw learner identifiers, and run only the analytics needed for the user's stated purpose.

Risk: The CLI sends default usage telemetry tied to a platform user id or persistent anonymous id.

Mitigation: Set AI_SHIFU_SKILL_TELEMETRY=off before running CLI commands for privacy-sensitive or offline work.

Risk: Saved authentication tokens may be present in local skill files or shared workspaces.

Mitigation: Avoid storing tokens in shared workspaces and use the skill's verification and SMS login flow rather than reading tokens directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Skill router](artifact/SKILL.md)
- [Course design intake](artifact/references/course-design-intake.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [Analytics overview](artifact/references/analytics/overview.md)
- [Analytics privacy and presentation](artifact/references/analytics/privacy-and-presentation.md)
- [CLI reference](artifact/references/cli/cli-reference.md)
- [Session controls](artifact/references/session-controls.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline MarkdownFlow content, JSON/DSL bodies, shell commands, course files, and concise operational reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local course directories and invoke AI-Shifu CLI commands for authentication, publishing, management, image upload, and analytics.]

## Skill Version(s):

1.2.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
