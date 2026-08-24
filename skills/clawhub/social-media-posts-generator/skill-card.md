## Description:

Generates multi-page social media post and poster carousels from prompts, templates, styles, asset sizes, and optional reference images using the Craftsman Agent image_generator API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to generate social media carousels, posters, presentation assets, app-store images, icons, logos, and edited photos from prompts, design settings, and optional uploaded images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, design metadata, and uploaded image content are sent to documented third-party services.

Mitigation: Avoid submitting secrets, private documents, or regulated data unless the provider's handling practices have been reviewed.

Risk: The skill requires a OneKey gateway credential for API access.

Mitigation: Use a scoped or rotatable OneKey credential where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/social-media-posts-generator)
- [Craftsman image generator console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [Craftsman website](https://craftsman-agent.aiagenta2z.com)
- [DeepNLP workspace keys](https://deepnlp.org/workspace/keys)
- [OneKey Agent Gateway router](https://agent.deepnlp.org/agent_router)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API request guidance for image-generation workflows and may return generated image URLs, workspace share URLs, page metadata, and editable layer data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
