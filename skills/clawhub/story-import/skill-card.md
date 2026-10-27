## Description:

将已有小说反向整理为可继续写作的项目，按篇幅分别生成长篇或短篇所需的正文、设定与大纲。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

小说作者和写作助手使用此技能导入已完成或写到一半的作品，将原稿整理成可供后续写作、审查和续写的项目。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Importing manuscripts saves their text locally and creates or changes story project files.

Mitigation: Confirm the source and destination with the author and review or back up existing project files before import.

Risk: Bundled validation and tracking scripts run locally, and activation changes the selected project.

Mitigation: Review script execution and confirm the intended project before setting .active-book.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-import)
- [Project link in skill metadata (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Length routing rules](references/length-routing.md)
- [Long-form project mapping](references/structure-mapping-long.md)
- [Short-form project mapping](references/structure-mapping-short.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Project files, Guidance]

**Output Format:** [Local manuscript and writing-project files, plus a Markdown import report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local story folders and sets .active-book for the imported project.]

## Skill Version(s):

1.0.32 (source: ClawHub release metadata; bundled SKILL.md frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
