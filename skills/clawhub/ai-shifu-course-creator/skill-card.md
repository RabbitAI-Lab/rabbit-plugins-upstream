## Description:

Create, edit, review, publish, manage, or analyze AI-Shifu (AI师傅) courses and their Teaching Prompts and Course Prompts in MarkdownFlow (MDF). Use for course materials, lesson design, interactions, course memory, images, deployment, platform administration, learner progress, learner profile distributions, orders, revenue, and credit-consumption questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators and administrators use this skill to design, author, edit, publish, and manage AI-Shifu courses, and to review course and learner analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Whole-course replacement can leave a course incomplete and does not preserve existing lesson access restrictions.

Mitigation: Prefer lesson-level updates for content edits; back up course content and access settings before import, then verify replacement permissions before publication.

Risk: Selected images are uploaded to the configured platform, and credentials persist locally.

Mitigation: Confirm the intended platform before uploading and protect the local profile that stores credentials.

Risk: Server defaults and backend privacy enforcement are unverified.

Mitigation: Review platform privacy and access settings before using sensitive learner data or opening a course to learners.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Build and import](artifact/references/build-and-import.md)
- [Course synchronization](artifact/references/course-sync.md)
- [Course analytics guide](artifact/references/analytics/guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Analysis, Guidance, Files]

**Output Format:** [MarkdownFlow and Markdown content, CLI commands, and course files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update course content and platform settings according to the requested task.]

## Skill Version(s):

2.2.0 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
