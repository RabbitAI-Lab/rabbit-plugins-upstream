## Description:

PDF 转视频、PDF 转讲解视频、PDF 生成视频——解析 PDF、大纲、分镜、配音、合成、校验。当用户给一份 PDF、想要讲解视频 / 报告解读 / 课件 / 培训视频时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators can turn a PDF into an explainer, report, courseware, or training video through a project-based chat workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires dLazy authentication and includes organization project-listing steps.

Mitigation: Confirm the account and organization context before logging in or listing projects; keep the API key in the CLI's user-restricted configuration or environment and rotate it if exposed.

Risk: PDFs and other attached local files are uploaded to dLazy media storage for processing.

Mitigation: Review document contents and confirm they are permitted for this service before attaching files, especially when they contain sensitive information.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Generated video with conversational text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attached local files are uploaded to dLazy media storage for processing; project sessions can be continued by project ID.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
