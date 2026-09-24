## Description:

智能图片换装，上传模特图和服装图后通过 api.a7w.cn 生成试穿效果，并支持提交任务与查询结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to call a third-party AI try-on service from an agent workflow, submit model and garment image URLs, and retrieve generated result images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use a saved a7w API key to call marketplace plugins beyond the AI try-on endpoint.

Mitigation: Use a limited or easily revocable key, review requested plugin and API names before execution, and revoke the key if it is exposed.

Risk: The client can redirect the API key to an overridden host through --host or A7W_HOST.

Mitigation: Keep the default api.a7w.cn host unless the alternate destination is fully trusted.

Risk: Submitted model and garment image URLs are processed by a third-party service and calls may consume account points.

Mitigation: Submit only images you have consent to process, check account costs before use, and avoid repeated async submissions for the same task.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [Submit API](references/api-submit.md)
- [Query API](references/api-query.md)
- [General Notes](references/通用说明.md)
- [a7w API platform](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided api.a7w.cn API key; async calls may return task IDs before result images are ready.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
