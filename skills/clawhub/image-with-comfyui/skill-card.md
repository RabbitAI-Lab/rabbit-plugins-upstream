## Description:

Calls a ComfyUI server to generate images, edit images, and create short image-to-video outputs using bundled workflows for Z-Image, SD3.5 Medium, Qwen Image Edit, and Wan2.2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route image generation, image editing, and image-to-video requests through a configured ComfyUI endpoint and return the generated media to the requesting session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, workflow JSON, and source images for image-to-image or image-to-video jobs are sent to the configured ComfyUI endpoint.

Mitigation: Keep the default loopback endpoint unless you control and trust the remote server, and avoid sensitive images unless that data flow is acceptable.

Risk: Generated media is retained in the configured local output directory.

Mitigation: Review the output location before use and periodically clean generated media, especially for sensitive content.

## Reference(s):

- [Image With Comfyui ClawHub listing](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [WAS Node Suite for ComfyUI](https://github.com/WASasquatch/was-node-suite-comfyui)
- [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Generated image or video files with concise status, warning, or error text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved under the configured output directory; delivery staging files are removed after successful send.]

## Skill Version(s):

1.7.1 (source: server release metadata and SKILL.md openclaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
