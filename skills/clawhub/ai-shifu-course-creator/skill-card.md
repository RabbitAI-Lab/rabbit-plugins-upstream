## Description:

Create, edit, publish, and manage AI-Shifu courses and their MarkdownFlow materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators and administrators use this skill to design and revise lessons, Teaching Prompts, and Course Prompts; review, publish, and manage courses; and answer questions about learner progress and course analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Whole-course imports delete and recreate lessons and reset access and visibility to platform defaults.

Mitigation: Prefer individual lesson updates; back up the course before whole-course replacement and verify access and visibility afterward.

Risk: Publishing or course-management actions may affect the wrong service account or publish content before it is ready.

Mitigation: Authorize only the intended service and account, and review completed content before approving publication.

Risk: Agent and version usage metadata may be attached to business requests.

Mitigation: Set SHIFU_DISABLE_ANALYTICS=1 to disable that usage metadata when desired.

Risk: First use may be blocked by a missing configuration template.

Mitigation: Obtain the required configuration template before first use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Course management](references/course-management.md)
- [Teaching Prompt authoring](references/teaching-prompt.md)
- [Course Prompt authoring](references/course-prompt.md)
- [Analytics privacy and presentation](references/analytics/privacy-and-presentation.md)
- [CLI reference](references/cli/cli-reference.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Analysis, Shell commands, Configuration instructions]

**Output Format:** [MarkdownFlow course materials and prompts, prose guidance and analysis, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include course files and operational steps for course publishing, management, or analytics.]

## Skill Version(s):

2.1.1 (source: skill frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
