## Description:

Uses the Flyelep AI Tool API to redraw selected areas of an image from a text prompt and, when provided, a reference replacement image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare image inpainting requests, upload local images when needed, and call Flyelep to replace backgrounds or redraw specified image regions while preserving the intended subject.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided images and edit prompts to Flyelep's external API.

Mitigation: Use it only for images and prompts suitable for Flyelep processing, and avoid sensitive private content unless that transfer is acceptable.

Risk: The security evidence notes that uploaded local images become persistent public URLs according to the skill text.

Mitigation: Prefer already public, non-sensitive image URLs or use the provider's deletion or retention workflow when public persistence is not acceptable.

Risk: The skill requires a Flyelep secretKey at runtime.

Mitigation: Ask the user for the key only at execution time and do not store it in skill files, examples, or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-partial-redrawing)
- [Flyelep control board](https://www.flyelep.cn/controlboard)
- [Flyelep partial redrawing API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/partialRedrawing)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and curl examples plus a returned image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a runtime Flyelep secretKey and public image URLs; local uploads may become persistent public URLs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
