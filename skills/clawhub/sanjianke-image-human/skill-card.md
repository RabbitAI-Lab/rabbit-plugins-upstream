## Description:

全驱动数字人，基于图片和参考音频生成自然稳定的数字人视频，支持提交任务和查询任务，并需要使用者自备 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External developers and content automation users use this skill to submit image-and-audio driven digital-human video jobs to api.a7w.cn and query the resulting task status or output. It is intended for users who already have an a7w account, API key, and account balance for paid API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided API key that can spend the user's a7w account balance.

Mitigation: Install and run it only when intending to use the a7w service; keep the key out of repositories, monitor charges, and revoke or rotate the key if it may be exposed.

Risk: The bundled client is broader than the advertised image_human workflow and can list schemas or call other marketplace APIs available to the key.

Mitigation: Use the client only with the documented image_human submit and query commands unless broader marketplace access is explicitly intended.

Risk: The client accepts host overrides through --host and A7W_HOST, which could redirect credentials if an untrusted host is used.

Mitigation: Keep the default api.a7w.cn host and avoid untrusted --host or A7W_HOST values.

Risk: Submitted image, voice, or private media URLs are processed by a third-party service and may trigger billing.

Mitigation: Submit only media the user is authorized to process, avoid sensitive face or voice data unless third-party processing is acceptable, and review content compliance before use.

Risk: Asynchronous submissions may freeze or consume points, and repeated submissions of the same job can create duplicate charges.

Mitigation: Use --no-wait or task queries to track an existing task instead of resubmitting, and verify pricing and balance before high-volume use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/2253128/skills/sanjianke-image-human)
- [Getting started](references/getting-started.md)
- [Submit task API](references/api-submit.md)
- [Query task API](references/api-query.md)
- [General api.a7w.cn guidance](references/通用说明.md)
- [api.a7w.cn service](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands; client command results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The submit workflow can return asynchronous task IDs and, after polling, video URLs and usage metadata from the third-party API.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
