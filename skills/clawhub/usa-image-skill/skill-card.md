## Description:

使用 usa0.top 的 OpenAI 兼容 GPT Images API 生成或编辑图片，支持文生图、本地或远程参考图、多图编辑和批量输出；当用户首次使用、询问安装配置或缺少密钥时，指导用户前往 https://usa0.top 获取生图分组的 API Key，并安全地配置 USA_API_KEY 环境变量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tkxs](https://clawhub.ai/user/tkxs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate or edit images through the usa0.top OpenAI-compatible Images API, including text-to-image, image-to-image, multi-reference, and batch image workflows. It also guides users through safe API key configuration when USA_API_KEY is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and request content are sent to the configured image API endpoint.

Mitigation: Use a dedicated, revocable usa0.top image-generation API key and avoid --base-url unless the destination is explicitly trusted.

Risk: Prompts and reference images may contain sensitive or unauthorized content.

Mitigation: Avoid submitting sensitive prompts or images, and only send content the user is authorized to process.

Risk: Passing an API key on the command line can expose it through shell history or process inspection.

Mitigation: Prefer USA_API_KEY environment configuration or the Windows secure configuration window; use --api-key only when the user explicitly accepts the risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tkxs/skills/usa-image-skill)
- [USA-0 image API service](https://usa0.top)
- [USA-0 API documentation](https://usa0.top/docs)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Image files with Markdown and inline shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally, usually under ./generated, and the script prints MEDIA lines with absolute output paths.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
