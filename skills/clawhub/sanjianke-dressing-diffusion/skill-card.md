## Description:

智能图片换装，上传模特图和服装图，AI 自动完成试穿效果生成，支持上衣、下装、全身换装，并提供提交任务和查询结果的 a7w API client workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to configure an a7w API key, submit model and garment image URLs for AI clothing try-on generation, and query asynchronous task results. It is useful for image-generation workflows that need command-line access to the dressing_diffusion plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can use a paid a7w API key and may spend account points.

Mitigation: Use a dedicated key with an appropriate balance, monitor usage, and avoid repeated submissions of the same task.

Risk: The bundled client is broader than a clothing try-on workflow and can call arbitrary a7w plugins.

Mitigation: Use explicit dressing_diffusion commands and review commands before execution.

Risk: Changing --host or A7W_HOST can send credentials and requests to a different endpoint.

Mitigation: Keep the default api.a7w.cn endpoint unless the destination is fully trusted.

Risk: Submitting identifiable personal images can expose sensitive personal data to a third-party service.

Mitigation: Submit personal images only with consent and after confirming the service's data handling terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-dressing-diffusion)
- [Getting started](references/getting-started.md)
- [Submit dressing task API](references/api-submit.md)
- [Query dressing result API](references/api-query.md)
- [a7w API platform](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with bash examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled client emits JSON to stdout and may save JSON results when an output file is requested; API calls may spend the user's a7w account points.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
