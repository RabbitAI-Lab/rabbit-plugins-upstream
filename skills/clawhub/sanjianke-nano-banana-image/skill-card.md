## Description:

图片生成与编辑应用，支持文生图、图生图和多规格模型选择，并提供创建图片任务和查询图片任务的调用封装。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit nano-banana image generation or editing jobs through the a7w API marketplace, then poll task status and retrieve generated image results. Users must provide their own api.a7w.cn API key and are responsible for account charges and content review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included client can access other a7w marketplace apps and recent task metadata available to the user's API key, beyond the advertised nano-banana image workflow.

Mitigation: Use a dedicated low-balance API key for this skill, review commands before execution, and avoid granting broader account access than needed.

Risk: Overriding --host or A7W_HOST can send the user's API key to a non-default endpoint.

Mitigation: Keep the default https://api.a7w.cn endpoint unless the replacement endpoint is fully trusted, and do not share API keys through chat or committed files.

Risk: Paid asynchronous submissions may consume account points and generated images may require policy or compliance review.

Mitigation: Check model and resolution pricing before submission, avoid duplicate task submissions, and review generated content before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-nano-banana-image)
- [Getting Started](references/getting-started.md)
- [Submit API Reference](references/api-submit.md)
- [Query API Reference](references/api-query.md)
- [a7w API Marketplace](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous image-generation jobs return task IDs and require polling; client output is JSON on stdout with human-readable status on stderr.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
