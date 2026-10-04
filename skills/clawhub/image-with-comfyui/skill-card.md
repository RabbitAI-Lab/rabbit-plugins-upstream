## Description:

Generate and edit images, animate images into videos, and turn character images into 3D meshes using a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request generated or edited images, short videos, and 3D character meshes from a ComfyUI server they configure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected source images are sent to the configured ComfyUI endpoint.

Mitigation: Keep the default localhost endpoint or use a server you control; avoid sending sensitive images to an untrusted endpoint.

Risk: Generated media is saved to a local output directory.

Mitigation: Use a trusted output directory and review access to saved media.

Risk: Manual installation of ComfyUI models or nodes can introduce unreviewed code or files.

Mitigation: Review model and node sources before installing; prefer environment variables for API keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Skill README](artifact/README.md)
- [CLI usage reference](artifact/references/cli-reference.md)
- [Qwen-Image 2.1 model files](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main?recursive=true)

## Skill Output:

**Output Type(s):** [Images, Video, 3D mesh files]

**Output Format:** [JPG or PNG images, video files, and ZIP-packaged GLB meshes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are saved locally for delivery to the user.]

## Skill Version(s):

3.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
