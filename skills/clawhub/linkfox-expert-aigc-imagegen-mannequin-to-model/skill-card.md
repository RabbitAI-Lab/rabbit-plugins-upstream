## Description:

人台换模特图生成：传入人台图以及可选模特或背景参考图，生成真人模特穿着该服装的电商展示图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to turn clothing mannequin photos into model-worn product images for storefront and catalog presentation. The skill is intended for mannequin inputs, with optional reference images for model identity or background style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, uploaded images, generated outputs, and API credentials through LinkFox-controlled services.

Mitigation: Use it only in environments where LinkFox is trusted with that data, and avoid private, regulated, or proprietary images unless remote processing and public upload are approved.

Risk: The bundled onboarding flow can involve phone-number registration, API-token setup, and possible billing or payment handling.

Mitigation: Prefer self-service credential setup and review any credential, phone-number, or billing flow before allowing an agent to handle it.

Risk: The workflow relies on model interpretation of mannequin images and may misread clothing type, fit, color, texture, or complex accessories.

Mitigation: Review generated images before use in commerce materials, provide clearer input photos or customer keywords when needed, and rerun with a different provider if clothing fidelity is insufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-imagegen-mannequin-to-model)
- [Workflow reference](artifact/references/workflow.md)
- [Data fields reference](artifact/references/data-fields.md)
- [Image generation API reference](artifact/skills/linkfox-aigc-imagegen/references/api.md)
- [Text generation API reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)
- [Image generation onboarding reference](artifact/skills/linkfox-aigc-imagegen/references/onboarding.md)
- [Text generation onboarding reference](artifact/skills/linkfox-aigc-textgen/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Files, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; runtime output is local generated-image paths or JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one model-worn image per run and may save raw API responses locally for troubleshooting.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
