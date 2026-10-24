## Description:

Create, edit, review, publish, manage, or analyze AI-Shifu courses and their Teaching Prompts and Course Prompts in MarkdownFlow (MDF).

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, educators, and administrators use this skill to design and review AI-Shifu course content, create MarkdownFlow course materials, manage deployment, and analyze authorized course and learner data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Course creation and edits may deploy automatically, while whole-course re-import can reset lesson permissions and visibility.

Mitigation: Specify local-only or unpublished-draft scope when appropriate. Prefer individual lesson updates for existing courses; back up the course and verify permissions and visibility after a whole-course re-import.

Risk: Course administration and analytics involve access to course and learner data.

Mitigation: Use an account authorized for the intended courses and learner data. Set SHIFU_DISABLE_ANALYTICS=1 to disable optional agent/version reporting.

Risk: Use may be blocked if the required environment template is missing.

Mitigation: Resolve the missing environment template before use.

## Reference(s):

- [AI-Shifu Course Creator on ClawHub](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Publisher profile](https://clawhub.ai/user/heshaofu2)
- [Course prompt guidance](references/course-prompt.md)
- [CLI reference](references/cli/cli-reference.md)
- [Analytics guide](references/analytics/guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Code, Shell commands, Analysis]

**Output Format:** [MarkdownFlow course materials, course files, command output, and written analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update course drafts and publish when requested or implied by the task; scope depends on the user's instructions.]

## Skill Version(s):

2.1.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
