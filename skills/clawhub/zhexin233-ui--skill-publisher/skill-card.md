## Description:

将本地技能一键打包、生成中文 PDF 说明文档、发布到 ClawHub，并自动截取发布页截图与链接，形成「创建→发布→文档→留证」的完整闭环。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhexin233-ui](https://clawhub.ai/user/zhexin233-ui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to validate a local ClawHub skill package, generate a Chinese PDF description, publish it to the ClawHub public marketplace, and preserve the published URL and screenshot as release evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles ClawHub API tokens during publishing.

Mitigation: Prefer environment variables or scoped short-lived tokens, and avoid exposing tokens in command history or shared logs.

Risk: Publishing uploads local skill contents to a public marketplace.

Mitigation: Review the exact skill directory and generated ignore rules before publishing.

Risk: The workflow runs external CLI and browser tooling.

Mitigation: Use trusted, pinned local dependencies and review tool output before treating the publish result as complete.

Risk: The helper may mutate project ignore files.

Mitigation: Inspect .clawhubignore changes before relying on them for release packaging.

## Reference(s):

- [Published ClawHub skill page](https://clawhub.ai/zhexin233-ui/skills/skill-publisher)
- [ClawHub](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and Python snippets; generated release artifacts may include a PDF, public URL, and screenshot path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ClawHub API token and local tools for PDF generation, publishing, and browser screenshots.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
