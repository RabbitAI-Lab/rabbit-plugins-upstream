## Description:

Helps agents query smart-clip templates and submit a7w video-generation jobs for talking-head, material mixcut, and news-style videos using a user-provided API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to configure an a7w API key, inspect smart-clip API schemas, submit video editing tasks, and retrieve task results as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the user's a7w API key beyond the advertised smart-clip video APIs.

Mitigation: Review the skill before installation and use a limited or disposable a7w API key when possible.

Risk: Changing --host or A7W_HOST could send the API key to an untrusted endpoint.

Mitigation: Keep the default api.a7w.cn endpoint unless a trusted replacement endpoint is required and verified.

Risk: Untrusted callbackUrl values may cause task notifications to be sent to unintended receivers.

Mitigation: Use only callback URLs controlled by the user or organization running the task.

Risk: API calls can consume points or balance on the user's a7w account, including asynchronous jobs that freeze points on submission.

Mitigation: Check parameters before submitting jobs, avoid duplicate submissions, and monitor task costs with the client output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-smart-clip)
- [Getting started](references/getting-started.md)
- [Template list API](references/api-template.md)
- [Template detail API](references/api-template_detail.md)
- [Talking-head mixcut API](references/api-realman_broadcast.md)
- [Material mixcut API](references/api-broadcast_mixcut.md)
- [News-style video API](references/api-news_mixcut.md)
- [a7w compute marketplace](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, video URLs, task status, duration, dimensions, point costs, and error details returned by a7w API calls.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
