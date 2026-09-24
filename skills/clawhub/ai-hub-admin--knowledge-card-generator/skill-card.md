## Description:

AI Knowledge Card Image Generator Skills to Generate Multi-Page Image Carousels from Templates such as Knowledge Card Sota Models Nano Banana, Nano Banana-2 ,Imagen-2 and more are available

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the Craftsman Agent image generation API and produce editable multi-page knowledge card image carousels from prompts, reference images, templates, asset sizes, styles, and design configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, reference images, and design configuration to third-party DeepNLP and Craftsman Agent services.

Mitigation: Avoid secrets, regulated data, private images, and sensitive prompts unless the service terms, access controls, and share URL exposure are acceptable.

Risk: The skill documents an unpinned `npx onekey` CLI path while using an API key.

Mitigation: Prefer the documented curl/API path or use a pinned, verified OneKey CLI version with a low-privilege, revocable API key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/knowledge-card-generator)
- [Publisher profile](https://clawhub.ai/user/ai-hub-admin)
- [Craftsman Image Generator Console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [Craftsman Website](https://craftsman-agent.aiagenta2z.com)
- [DeepNLP workspace keys](https://deepnlp.org/workspace/keys)
- [OneKey agent router endpoint](https://agent.deepnlp.org/agent_router)
- [Example generated session](https://craftsman-agent.aiagenta2z.com/app/sessions/share/547083a4-5e38-4e4e-ba78-300cadb88b11)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API payloads and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream service can return generated image URLs, a share URL, page layer data, session metadata, and exportable carousel assets.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
