## Description:

Generates images with Alibaba Cloud DashScope Qwen-Image models from Chinese or English prompts, with configurable model, size, negative prompt, prompt extension, watermark, and seed settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn user image-generation requests into DashScope Qwen-Image API calls and return generated image URLs. It is suited for workflows that need prompt-based image creation with selectable Qwen image models and generation parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, negative prompts, and generation settings are sent to Alibaba Cloud DashScope and may contain sensitive information if users include it.

Mitigation: Do not include secrets, personal data, or confidential material in image prompts or generation parameters.

Risk: DashScope image-generation calls may incur API costs and can be rate-limited or rejected for invalid parameters.

Mitigation: Use a valid DASHSCOPE_API_KEY, review model and size settings before execution, and reduce request frequency when rate limits occur.

Risk: Generated image result URLs are temporary according to the artifact documentation.

Mitigation: Save required generated images promptly after receiving the response URL.

## Reference(s):

- [千问文生图 API 详细参考](references/api.md)
- [Alibaba Cloud Model Studio API key documentation](https://help.aliyun.com/zh/model-studio/get-api-key)
- [DashScope multimodal generation endpoint](https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation)
- [DashScope international multimodal generation endpoint](https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation)
- [DashScope asynchronous image synthesis endpoint](https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis)
- [DashScope task status endpoint](https://dashscope.aliyuncs.com/api/v1/tasks/{task_id})

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, Guidance]

**Output Format:** [Markdown with bash and JSON examples, plus generated image URLs from the API response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image URLs are described as temporary and should be saved promptly.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
