## Description:

AI Knowledge Card Image Generator Skills to Generate Multi-Page Image Carousels from Templates such as Knowledge Card Sota Models Nano Banana, Nano Banana-2 ,Imagen-2 and more are available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to call the Craftsman Agent image_generator API and generate editable knowledge-card images, slides, and social-media carousel assets from prompts, reference images, templates, and design configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded images, and design configuration are sent to third-party DeepNLP/Craftsman cloud services.

Mitigation: Avoid confidential, regulated, or secret content unless the service and its data handling are approved for that data.

Risk: The artifact includes an unpinned npx CLI invocation.

Mitigation: Use the explicit curl API example or pin and review the CLI package before executing it.

Risk: The skill requires a OneKey access key.

Mitigation: Store DEEPNLP_ONEKEY_ROUTER_ACCESS in a managed secret store or scoped environment and avoid committing it to files or logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/knowledge-card-generator)
- [Craftsman Image Generator Console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [Craftsman Workspace](https://craftsman-agent.aiagenta2z.com/workspace)
- [DeepNLP OneKey Workspace Keys](https://deepnlp.org/workspace/keys)
- [OneKey Router API Endpoint](https://agent.deepnlp.org/agent_router)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown instructions with bash and JSON examples; API responses include JSON containing generated image URLs, share URLs, page metadata, and editable layer configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DEEPNLP_ONEKEY_ROUTER_ACCESS key and sends prompts, images, and design configuration to third-party cloud services.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
