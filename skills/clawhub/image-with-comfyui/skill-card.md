## Description:

Helps agents generate, edit, and animate images through a configured ComfyUI server using bundled image and video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to generate images from prompts, edit or combine source images, and animate images as short videos with a configured ComfyUI server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and workflows are sent to the configured ComfyUI server; editing and animation also upload source images.

Mitigation: Keep the default loopback endpoint or use only a trusted server you control; avoid sending sensitive source material to an untrusted endpoint.

Risk: Generated media and delivery staging copies may contain sensitive content.

Mitigation: Review output and staging directories and remove sensitive media when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Setup and usage](artifact/README.md)
- [Model download sources](artifact/MODEL_URL.txt)
- [Workflow attribution](artifact/references/attribution.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with generated image or video attachments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally before delivery.]

## Skill Version(s):

2.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
