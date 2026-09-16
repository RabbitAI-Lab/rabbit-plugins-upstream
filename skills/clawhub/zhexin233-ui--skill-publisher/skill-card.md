## Description:

将本地技能一键打包、生成中文 PDF 说明文档、发布到 ClawHub，并自动截取发布页截图与链接，形成「创建→发布→文档→留证」的完整闭环。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhexin233-ui](https://clawhub.ai/user/zhexin233-ui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill to validate a local skill directory, generate a Chinese PDF description, publish the package to ClawHub, and retain the resulting page URL and screenshot as release evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing can upload unintended local files or generated artifacts.

Mitigation: Confirm the selected skill directory contains only intended public files and review or create .clawhubignore before publishing.

Risk: Publishing requires a ClawHub API token.

Mitigation: Use a ClawHub token with only the access needed for publishing and avoid exposing it in shared logs or skill files.

Risk: The workflow intentionally generates a PDF, captures a screenshot, and uploads to a public ClawHub page.

Mitigation: Treat the generated PDF, screenshot, and public upload as intentional release outputs and review them before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhexin233-ui/skills/skill-publisher)
- [ClawHub](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash and Python examples, plus generated PDF and screenshot file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a public ClawHub skill URL, generated PDF path, screenshot path, and publishing status.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
