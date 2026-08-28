## Description:

多功能免费工具箱 - 图片处理、PDF转换、数据换算、文本工具、开发工具、视频工具、教育、生活娱乐、实用小工具、系统工具、AI办公。11大模块49个工具。v3.9 统一CLI与体验重构：dgngjx CLI(argparse) + registry.json注册表 + 49工具参数化 + 安全分级 + 无人值守。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill as a multipurpose local toolbox for data conversion, text utilities, media and PDF processing, system utilities, and AI office workflows through natural-language prompts or the dgngjx CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The toolbox can process local files broadly, including sensitive Office and media files.

Mitigation: Review selected input and output paths before running tools, keep confirmation prompts enabled for sensitive files, and inspect generated outputs before sharing.

Risk: The history and configuration features can persist user content on the local machine.

Mitigation: Disable or clear history for confidential work and avoid recording sensitive inputs or outputs.

Risk: Meeting workflows may upload audio to a transcription API endpoint.

Mitigation: Use local Whisper or manual text modes for private meetings unless the API endpoint and data handling are explicitly trusted.

Risk: Unattended --yes mode can skip non-dangerous confirmations.

Mitigation: Avoid --yes and DGNGJX_ASSUME_YES for sensitive files, Office documents, or workflows that need human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/dgngjx-skill)
- [Publisher profile](https://clawhub.ai/user/fyniujin)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, plain text, JSON, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by selected tool and may include local file transformations, generated reports, hashes, CLI JSON, or configuration/history updates.]

## Skill Version(s):

3.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
