## Description:

Generate or edit AI images via Pixmind API (text-to-image and image-to-image).

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, vary, or upscale images through Pixmind models from natural-language prompts and optional reference image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation settings, and reference image URLs are sent to Pixmind's remote API.

Mitigation: Use the skill only when external Pixmind processing is acceptable, and avoid secrets, private internal URLs, and sensitive personal content in prompts or reference images.

Risk: The skill requires a PIXMIND_API_KEY.

Mitigation: Scope the key to Pixmind, provide it through the environment, and avoid exposing it in prompts, shared command text, or logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fuyunzhishang/skills/pixmind-image)
- [Pixmind Homepage](https://www.pixmind.io)
- [Pixmind API Key Management](https://www.pixmind.io/api-keys)
- [Pixmind Image Generation Endpoint](https://aihub-admin.aimix.pro/open-api/v1/image/generate)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON or image URL results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY; generation may return a task ID first and generated image URLs after polling.]

## Skill Version(s):

2.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
