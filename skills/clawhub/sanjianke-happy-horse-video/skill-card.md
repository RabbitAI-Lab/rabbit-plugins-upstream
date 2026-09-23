## Description:

三剪客 · Happy Horse helps agents submit, create, and query Happy Horse text-to-video and image-to-video jobs through the a7w API using a user-provided API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to call Happy Horse video-generation APIs from an agent, including asynchronous task submission, task creation, and status/result queries. Users must provide their own api.a7w.cn API key and are responsible for account costs and generated-content review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can send the bearer API key to a user-configured host through --host or A7W_HOST.

Mitigation: Use the default api.a7w.cn endpoint unless you fully trust the replacement host, and review local configuration and environment variables before running commands.

Risk: The bundled generic CLI can use a paid API key beyond the named Happy Horse endpoints.

Mitigation: Limit use to the documented happy_horse submit, create, and query calls unless you intentionally choose to use other a7w marketplace commands.

Risk: Repeated video-generation submissions can consume account points and generated outputs may require content review.

Mitigation: Avoid duplicate submissions, check task status before retrying, monitor point usage, and review generated content for policy and rights compliance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-happy-horse-video)
- [Getting started: API key setup](references/getting-started.md)
- [Happy Horse submit API](references/api-submit.md)
- [Happy Horse create API](references/api-create.md)
- [Happy Horse query API](references/api-query.md)
- [a7w API marketplace](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include asynchronous task IDs, video URLs, task status, duration, dimensions, point costs, and API error details returned by a7w.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
