## Description:

Creates, edits, reviews, publishes, manages, and analyzes AI-Shifu courses and their teaching and course prompts in MarkdownFlow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course authors and administrators use this skill to design AI-Shifu lessons, write MarkdownFlow prompts, manage course publication, and review course and learner analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated account can publish learner-facing courses without a CLI-enforced approval gate.

Mitigation: Independently verify the exact course and content before publication, and use an account trusted for publishing.

Risk: Course administration can change or archive existing courses.

Mitigation: Review the target course and requested changes before authorizing account access or making edits.

Risk: Raw learner question-and-answer analytics may expose sensitive learner information.

Mitigation: Limit raw learner Q&A access to justified support or moderation needs and share only necessary results.

## Reference(s):

- [AI-Shifu Course Creator release](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Teaching Prompt guidance](artifact/references/teaching-prompt.md)
- [MarkdownFlow syntax](artifact/references/markdownflow-syntax.md)
- [Course management](artifact/references/course-management.md)
- [Analytics privacy and presentation](artifact/references/analytics/privacy-and-presentation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown and MarkdownFlow course materials, with CLI guidance and analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update courses in an authenticated AI-Shifu account.]

## Skill Version(s):

2.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
