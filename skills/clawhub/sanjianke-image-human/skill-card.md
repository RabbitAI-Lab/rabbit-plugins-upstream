## Description:

全驱动数字人，基于图片和参考音频生成自然稳定的数字人视频，支持提交任务和查询任务，并需要使用者自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit and query image_human digital human video generation jobs through the a7w API using their own API key and account balance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required a7w API key may access or spend against more than only the image_human feature.

Mitigation: Use a key with the least practical permissions and balance, monitor usage, and revoke or rotate the key if unexpected activity appears.

Risk: Changing A7W_HOST or passing --host can direct authenticated requests to a non-default destination.

Mitigation: Use the default api.a7w.cn host unless the destination is fully trusted.

Risk: Submitting generation jobs consumes account points and duplicate submissions may create duplicate charges.

Mitigation: Review job parameters and costs before submission, prefer --no-wait plus task polling when appropriate, and avoid resubmitting the same task.

Risk: Generated digital human video content may require legal, consent, and content compliance review.

Mitigation: Review source media rights, consent, and generated output before publication or operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-image-human)
- [开始使用：注册、充值、配置 Key](references/getting-started.md)
- [全驱动数字人 · 提交任务](references/api-submit.md)
- [全驱动数字人 · 查询任务](references/api-query.md)
- [算力集市](https://api.a7w.cn/)
- [AI 插件市场](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write JSON results to a user-specified output path when --out is provided.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
