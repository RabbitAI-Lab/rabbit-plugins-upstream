## Description:

Use this skill to generate, edit, or animate images and videos through a configured ComfyUI server using Z-Image, SD3.5 Medium, Qwen Image Edit, and Wan2.2 workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route image generation, image editing, and image-to-video requests through an existing ComfyUI deployment. It is suited for agent workflows that need visual media output from text prompts or source images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded source images may be sent to the configured ComfyUI endpoint, which may be non-local.

Mitigation: Review or change COMFYUI_URL and config.json before use, use only trusted ComfyUI endpoints, and avoid sensitive photos unless endpoint control and retention are understood.

Risk: Generated files and edited source media may be retained by the configured endpoint or output directory.

Mitigation: Use an output location with appropriate access controls and clean up generated media according to the deployment's retention requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [ComfyUI WAS Nodes](https://github.com/WASasquatch/ComfyUI-WAS-Nodes.git)
- [ComfyUI Manager](https://github.com/comfyanonymous/ComfyUI-Manager.git)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime outputs are image or video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to the configured output directory and should be delivered as an attachment when appropriate.]

## Skill Version(s):

1.7.0 (source: server release metadata and OpenClaw frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
