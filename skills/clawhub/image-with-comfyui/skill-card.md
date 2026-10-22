## Description:

Helps agents generate and edit images, create videos, and turn images into 3D meshes through a configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents working with creators and developers use this skill to request image generation or edits, video generation, and image-to-3D conversion from a ComfyUI server they configure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, workflow data, and source images may be sent to the configured ComfyUI server.

Mitigation: Use a server you control or trust, and avoid sending sensitive images unless its handling is acceptable.

Risk: Generated media is saved locally before delivery and may persist in output or staging directories.

Mitigation: Review output locations and cleanup behavior before processing sensitive content.

Risk: Available server models may generate content outside the intended safety policy.

Mitigation: Use safe model sets when NSFW-capable models are not intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Setup and data handling](artifact/README.md)
- [Model download sources](artifact/MODEL_URL.txt)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown and plain text with local output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The commands save generated images, videos, or zipped 3D meshes locally for delivery.]

## Skill Version(s):

4.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
