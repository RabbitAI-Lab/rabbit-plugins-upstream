## Description:

Guides agents through GPT Image 2 multi-reference image generation with per-image role, allow, deny, ownership, identity, layout, and conflict rules to reduce identity or product cross-contamination through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and creative operators use this skill to prepare and run AI Hive GPT Image 2 jobs that combine 2-8 reference images while preserving approved identities, products, layouts, and scene constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys passed directly on the command line can be exposed through shell history or process listings.

Mitigation: Prefer AI_HIVE_API_KEY or the protected AI Hive config file, and avoid pasting API keys into shared terminals or logs.

Risk: Reference images are uploaded to AI Hive during generation.

Mitigation: Use only images that are authorized for upload and appropriate for the target AI Hive account.

Risk: Generated image jobs can preserve or transform people, products, logos, packaging, and text from references.

Mitigation: Review the preview contract and final image for identity, SKU, logo, quantity, layout, and unauthorized content before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/image-2-multi-reference-image)
- [AI Hive OpenAPI Endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown instructions with bash commands; preview and status commands can emit JSON, and completed jobs download PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 2-8 reference images and one GPT Image 2 output per compose job; may upload references to AI Hive and save PNG downloads locally.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
