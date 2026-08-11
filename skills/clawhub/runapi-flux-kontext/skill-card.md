## Description:

Generate and edit images with Flux Kontext through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through one-off Flux Kontext image generation or editing with the RunAPI CLI, and through SDK-based integration when adding Flux Kontext to applications or backend services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on RunAPI as an external provider for image generation and editing.

Mitigation: Review RunAPI suitability before installation and use environment or saved CLI authentication for agent runs.

Risk: RUNAPI_API_KEY is a credential when provided to the agent environment.

Mitigation: Treat the key as sensitive, avoid exposing it in prompts or logs, and prefer environment authentication or saved CLI config.

Risk: Generated file URLs are temporary and may expire.

Mitigation: Download and store generated assets in durable storage within 7 days when the output must be retained.

## Reference(s):

- [Flux Kontext model overview](https://runapi.ai/models/flux-kontext.md)
- [Flux Kontext homepage](https://runapi.ai/models/flux-kontext)
- [Black Forest Labs provider comparison](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Flux Kontext Pro variant](https://runapi.ai/models/flux-kontext/pro.md)
- [Flux Kontext Max variant](https://runapi.ai/models/flux-kontext/max.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, SDK package names, and request configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference temporary generated file URLs that should be downloaded to durable storage within 7 days.]

## Skill Version(s):

0.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
