## Description:

Grok 视频生成应用，支持快速视频生成和标准生成视频；支持创建视频任务、查询视频任务，并要求使用者提供自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to configure an a7w API key, submit Grok video generation jobs, poll task status, and retrieve generated video results through the bundled command-line client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the saved a7w API key for broader marketplace calls than the Grok-only framing suggests.

Mitigation: Use a dedicated low-balance a7w API key and restrict agent use to the Grok video submit and query workflows unless broader marketplace access is intended.

Risk: A configured host override could send the API key to an unintended destination.

Mitigation: Keep the default api.a7w.cn host and avoid A7W_HOST or --host unless the destination is fully trusted.

Risk: Prompts, private image URLs, and callback endpoints may be sent to the third-party video service during task submission.

Mitigation: Do not submit sensitive prompts, private media URLs, or callback endpoints that the user does not control.

Risk: The API key may be stored in local configuration or provided through the environment.

Mitigation: Protect the local config file and environment, avoid committing secrets, and rotate the key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-grok-video)
- [Publisher profile](https://clawhub.ai/user/2253128)
- [Getting started](references/getting-started.md)
- [Common instructions](references/通用说明.md)
- [Create video task API](references/api-submit.md)
- [Query video task API](references/api-query.md)
- [a7w compute marketplace](https://api.a7w.cn/)
- [a7w AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The client can persist a user-provided API key locally, submit asynchronous video generation jobs, poll task status, and optionally write returned JSON to a file.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata; artifact frontmatter is 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
