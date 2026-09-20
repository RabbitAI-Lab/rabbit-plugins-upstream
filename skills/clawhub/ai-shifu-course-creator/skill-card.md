## Description:

AI-Shifu Course Creator helps agents create, edit, optimize, deploy, manage, and analyze AI-Shifu courses using MarkdownFlow Teaching Prompts and Course Prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators and developers use this skill to turn source material into structured AI-Shifu courses, revise existing platform courses, publish or manage course metadata, and inspect course analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on an authenticated AI-Shifu account for course creation, publishing, management, and analytics.

Mitigation: Install and run it only for accounts and courses the operator intends to manage, and review authentication prompts and target course resolution before platform operations.

Risk: Course deployment can publish learner-facing content as part of the normal course creation workflow.

Mitigation: Review the generated course preview and the publish confirmation before approving deployment or publication.

Risk: Default CLI telemetry can associate usage events with a logged-in platform identity or a persistent local analytics ID.

Mitigation: Set AI_SHIFU_SKILL_TELEMETRY=off before use when usage events should not be tied to platform identity or local analytics state.

## Reference(s):

- [Skill definition](SKILL.md)
- [MarkdownFlow Spec](references/markdownflow.md)
- [Teaching Prompt](references/teaching-prompt.md)
- [Course Prompt](references/course-prompt.md)
- [New Course Deployment](references/deployment-workflow.md)
- [Platform Authentication](references/authentication.md)
- [Course Analytics](references/analytics/workflow.md)
- [Privacy & Presentation](references/analytics/privacy-and-presentation.md)
- [CLI Reference](references/cli/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with fenced code, shell commands, JSON/configuration snippets, and generated course artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require authenticated AI-Shifu account access for platform operations; usage telemetry can be disabled with AI_SHIFU_SKILL_TELEMETRY=off.]

## Skill Version(s):

1.2.9 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
