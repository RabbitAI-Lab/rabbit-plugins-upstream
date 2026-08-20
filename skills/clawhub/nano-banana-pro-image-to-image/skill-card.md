## Description:

Nano Banana Pro 图生图 helps agents transform reference images with Nano Banana Pro through AI Hive while preserving identity, product, spatial, composition, color, material, and lighting anchors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and creative operators use this skill to guide image-to-image generation workflows that preserve reference-image anchors while changing art direction, lighting, materials, styling, layout, or channel format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images supplied with --image are uploaded to AI Hive.

Mitigation: Use only images the operator has rights to process and avoid submitting sensitive or restricted images unless AI Hive handling is approved for that data.

Risk: An AI Hive API key may be stored locally or passed to the helper.

Mitigation: Keep the API key private, prefer controlled environment or configuration storage, and rotate the key if it may have been exposed.

Risk: Generated outputs are written to a local output directory.

Mitigation: Choose an output directory appropriate for the generated content and review saved files before reuse or distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-image-to-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with shell command examples; the helper script emits terminal text, JSON task data, and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-selected reference image for generation and uses an AI Hive API key.]

## Skill Version(s):

1.0.1 (source: server release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
