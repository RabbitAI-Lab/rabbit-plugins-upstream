## Description:

Create, edit, review, publish, manage, or analyze AI-Shifu courses and their MarkdownFlow prompts and learning materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heshaofu2](https://clawhub.ai/user/heshaofu2)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and course developers use this skill to design and review AI-Shifu courses, create MarkdownFlow prompts and course materials, and manage platform deployments or course analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Synchronization can overwrite local course structure and configuration edits without the backups described by the skill.

Mitigation: Keep an independent backup of the full course directory, especially structure.json and course-config.json, before synchronization. Prefer targeted lesson updates; whole-course re-import recreates lessons and resets permissions.

Risk: Platform credentials persist locally, and platform requests may include bounded agent and skill-version usage metadata.

Mitigation: Use a protected device, set SHIFU_DISABLE_ANALYTICS=1 to omit usage metadata, and log out to remove locally saved credentials when they are no longer needed.

## Reference(s):

- [AI-Shifu Course Creator release on ClawHub](https://clawhub.ai/heshaofu2/skills/ai-shifu-course-creator)
- [Teaching Design](artifact/references/teaching-design.md)
- [Existing Course Sync](artifact/references/course-sync.md)
- [CLI Reference](artifact/references/cli/cli-reference.md)
- [Platform Authentication](artifact/references/authentication.md)
- [Analytics Privacy and Presentation](artifact/references/analytics/privacy-and-presentation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Analysis]

**Output Format:** [Markdown and text, course files, CLI commands, or structured analytics results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the requested authoring, platform, or analytics task.]

## Skill Version(s):

2.2.2 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
