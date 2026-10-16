## Description:

Generates and edits images, animates images into video, and creates 3D meshes through a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ComfyUI users use this skill to create or edit images, produce video from images, and turn images into 3D meshes on a server they configure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, workflow definitions, and selected source images are sent to the configured ComfyUI server.

Mitigation: Use a ComfyUI server you control and verify its address before submitting sensitive content.

Risk: Generated media remains on local disk and may contain sensitive content.

Mitigation: Review access to the configured output directory and remove sensitive files when no longer needed.

Risk: An API key stored in configuration may be exposed to others with access to the file.

Mitigation: Supply the key through COMFYUI_APIKEY rather than storing it in config.json.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Setup and configuration](artifact/README.md)
- [Workflow attribution](artifact/references/attribution.md)
- [Qwen-Image 2.1 Turbo model weights](https://huggingface.co/abenzerps/Qwen-Image-2.1-Turbo-Quantized)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance and locally saved images, videos, and zipped GLB meshes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to the configured output directory.]

## Skill Version(s):

3.7.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
