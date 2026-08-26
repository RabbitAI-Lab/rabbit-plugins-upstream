## Description:

AI Generated 3D Models using SOTA APIs such as Tripo/Meshy/TripoSR/etc served on OneKey Agent Gateway by Craftsman Agent, useful for AI Game, Figurine, Stuffed Toy Generation

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to create and poll 3D generation tasks from text prompts, single images, or multi-view images. It supports workflows that produce downloadable 3D model assets and preview images through external 3D generation providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image URLs, generated asset metadata, and task details are sent to the OneKey gateway and downstream 3D generation providers.

Mitigation: Use non-confidential prompts and images unless policy allows third-party processing, and redact sensitive values before sharing logs or examples.

Risk: The skill requires a OneKey gateway access key for API calls.

Mitigation: Keep DEEPNLP_ONEKEY_ROUTER_ACCESS private and avoid embedding the key in shared commands, documentation, or generated artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/3d-generator)
- [Craftsman 3D Generator](https://craftsman-agent.aiagenta2z.com/app/3d-generator)
- [Craftsman 3D Generator Gallery](https://craftsman-agent.aiagenta2z.com/gallery/3d_generator)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration, code, markdown]

**Output Format:** [Markdown documentation with shell commands, JSON request and response examples, and API parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents creation and polling flows for text-to-model, image-to-model, and multi-view-to-model tasks.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
