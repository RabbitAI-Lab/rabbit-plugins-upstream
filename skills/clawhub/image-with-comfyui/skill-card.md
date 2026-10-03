## Description:

Generates and edits images, animates images into videos, and creates 3D meshes through a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images, turn images into short videos, and create 3D character meshes with their own ComfyUI server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected source images are sent to the configured ComfyUI endpoint.

Mitigation: Use localhost or a trusted HTTPS server, and avoid submitting sensitive content to untrusted endpoints.

Risk: Generated media remains on local storage after creation.

Mitigation: Review the output directory and remove sensitive media when no longer needed.

Risk: API keys stored in configuration files may be exposed.

Mitigation: Set COMFYUI_APIKEY in the environment instead of saving credentials in config files.

Risk: Manual installation of ComfyUI models or custom nodes introduces third-party software.

Mitigation: Review model and custom-node sources before installing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [CLI reference](references/cli-reference.md)
- [Workflow attribution](references/attribution.md)
- [ComfyUI authentication custom node](https://github.com/sunshinejnjn/comfyui-auth)

## Skill Output:

**Output Type(s):** [Images, Videos, 3D meshes, Text guidance]

**Output Format:** [PNG or JPEG images, video files, ZIP-packaged GLB meshes, and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally; 3D mesh delivery also includes a character image.]

## Skill Version(s):

3.5.0 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
