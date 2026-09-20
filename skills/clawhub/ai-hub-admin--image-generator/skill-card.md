## Description:

Generates AI poster images and editable multi-page image carousels from text prompts, templates, uploaded reference images, and design configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate AI posters, social media carousels, presentations, app-store images, icons, logos, and photo edits through a hosted web console, API, or CLI. It supports editable text and image layers, custom asset sizes, style prompts, and exportable workspace outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded images, generated content, and the DeepNLP/OneKey access key are sent to hosted external services.

Mitigation: Use scoped credentials, avoid sensitive or regulated content, and install only when external service processing is acceptable.

Risk: The artifact advertises watermark removal capability.

Mitigation: Avoid using watermark removal unless the user has rights to modify the source image and the use complies with applicable terms.

Risk: The documented `npx onekey` command can execute an unpinned npm package.

Mitigation: Pin and verify the package version before use, or run it in a restricted environment with a scoped key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/image-generator)
- [Craftsman Image Generator Console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [Craftsman Workspace](https://craftsman-agent.aiagenta2z.com/workspace)
- [DeepNLP Workspace Keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with bash and JSON examples; hosted service responses include JSON fields, generated image URLs, and share/workspace URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may include editable layered page data and exports such as PNG, PDF, or PPT via the hosted workspace.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
