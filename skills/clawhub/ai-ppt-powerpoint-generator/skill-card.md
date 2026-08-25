## Description:

Generates multi-page PowerPoint-style image carousels from text prompts and templates through the Craftsman image_generator API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the Craftsman image generation service for prompt-driven presentation, carousel, and poster assets with configurable page count, aspect ratio, and editable text layers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded reference images are sent to external DeepNLP/Craftsman services.

Mitigation: Use non-sensitive prompts and images unless the service terms and data-handling posture are acceptable for the intended use case.

Risk: The integration exposes broader image and photo-editing templates than the PowerPoint-focused name suggests.

Mitigation: Restrict use to intended presentation or carousel templates, and avoid broader editing modes such as photo editing or watermark removal unless explicitly permitted.

Risk: The skill requires a OneKey Gateway access key for API and CLI usage.

Mitigation: Store the access key in a secret manager or local environment variable, and avoid sharing it in prompts, generated artifacts, logs, or examples.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-hub-admin/skills/ai-ppt-powerpoint-generator)
- [Craftsman Image Generator Console](https://craftsman-agent.aiagenta2z.com/app/image-generator)
- [DeepNLP OneKey Access Keys](https://deepnlp.org/workspace/keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with bash commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referenced service can return image URLs, share URLs, editable slide layer data, and workspace exports such as PDF, PNG, or PPT.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
