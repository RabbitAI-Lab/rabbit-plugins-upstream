## Description:

Creates and edits images through the a7w nano_banana API, with support for text-to-image, image-to-image editing, model selection, task submission, and task querying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure an a7w API key, submit nano_banana image generation or editing jobs, and query asynchronous task results. It is intended for external users who bring their own a7w account, API key, and usage budget.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can send the user's a7w API key to a configurable host.

Mitigation: Use the default api.a7w.cn host unless a replacement endpoint is fully trusted; avoid --host and A7W_HOST for routine use.

Risk: Prompts, image URLs, task IDs, and generated outputs are submitted to a third-party marketplace API.

Mitigation: Do not submit sensitive prompts, private image URLs, or regulated content unless the user has approved that disclosure.

Risk: The API key controls paid marketplace usage and may expose the user's balance if leaked.

Mitigation: Store the key locally or in A7W_API_KEY, never commit it, and revoke or rotate it from the a7w account if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-nano-banana-image)
- [Getting started](references/getting-started.md)
- [Submit image task API](references/api-submit.md)
- [Query image task API](references/api-query.md)
- [General a7w plugin guidance](references/通用说明.md)
- [a7w compute marketplace](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation results are returned through a7w task responses, usually as image URLs in JSON.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
