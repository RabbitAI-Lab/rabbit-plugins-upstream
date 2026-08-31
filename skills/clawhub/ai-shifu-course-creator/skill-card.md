## Description:

AI-Shifu Course Creator helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses that use MarkdownFlow Teaching Prompts and Course Prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, operators, and developer-assisted authoring teams use this skill to build course structure, write MarkdownFlow prompts, deploy or manage AI-Shifu courses, and inspect live course analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage analytics can be tied to the user's AI-Shifu account or machine.

Mitigation: Review telemetry expectations before installing and set AI_SHIFU_SKILL_TELEMETRY=off for privacy-sensitive or offline runs.

Risk: The skill can perform live course mutations, including publishing, archiving, deleting, or importing existing course content.

Mitigation: Require the agent to ask for explicit confirmation before publish, archive, delete, or existing-course import operations.

Risk: A custom AI-Shifu base URL can redirect operations to an untrusted deployment.

Mitigation: Keep SHIFU_BASE_URL pointed only at a trusted HTTPS AI-Shifu deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [AI-Shifu application](https://app.ai-shifu.cn)
- [MarkdownFlow](references/markdownflow.md)
- [Course design intake](references/course-design-intake.md)
- [Teaching prompt](references/teaching-prompt.md)
- [Course prompt](references/course-prompt.md)
- [Deployment workflow](references/deployment-workflow.md)
- [Course management](references/course-management.md)
- [Analytics overview](references/analytics/overview.md)
- [Analytics privacy and presentation](references/analytics/privacy-and-presentation.md)
- [CLI reference](references/cli/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, CLI commands, and JSON DSL snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local course files and propose AI-Shifu CLI operations.]

## Skill Version(s):

1.2.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
