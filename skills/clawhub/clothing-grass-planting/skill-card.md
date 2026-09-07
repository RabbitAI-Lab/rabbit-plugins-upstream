## Description:

Generates social-commerce outfit image guidance that keeps a source outfit faithful while changing the model, pose, scene, lighting, camera angle, and crop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agents use this skill to prepare lifestyle social-commerce outfit generation prompts and commands. It is intended for owned or licensed outfit and reference images where garment details should stay consistent across new scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can copy a reference person's identity into social-style images, which may imply endorsement or create misleading likeness use.

Mitigation: Use only owned or licensed outfit and reference images, avoid copying real people without permission, and do not use outputs to imply endorsement or fabricate testimonials.

Risk: Provider selection and custom endpoint or binary overrides can route prompts and images through untrusted services.

Mitigation: Prefer default trusted provider endpoints, avoid ARK_BASE_URL and DLAZY_BIN unless they are controlled and trusted, and verify the dLazy CLI before use.

Risk: Watermark or provenance removal behavior may strip attribution or rights signals from third-party media.

Mitigation: Do not strip provenance, watermarks, or attribution from third-party media; keep rights and source records with generated assets.

Risk: Local outfit and reference images may be uploaded to the selected cloud provider during generation.

Mitigation: Review image rights and privacy before execution, avoid sensitive personal images, and select providers consistent with the user's data handling requirements.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [gpt-image-2 parameters](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, prompt templates, and image generation parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may save generated JPEG image files when executed; the documented default is 1024x1536 JPEG at medium quality with optional batch generation.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
