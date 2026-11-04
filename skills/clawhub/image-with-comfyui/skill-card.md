## Description:

Generate, edit, or animate images and videos, create transparent cutouts, and make 3D meshes through a configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers and other ComfyUI users can create or edit images, generate videos, extract transparent subjects, and create 3D mesh assets from prompts or source images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic cleanup can leave generated media on the ComfyUI server.

Mitigation: For sensitive media, check the server after each run and manually remove any leftovers.

Risk: Prompts and full source images are sent to the configured ComfyUI server.

Mitigation: Use a trusted ComfyUI server and HTTPS for remote connections.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Output delivery guidance](references/delivery.md)
- [Workflow attribution notes](references/attribution.md)

## Skill Output:

**Output Type(s):** [Images, Videos, 3D model files, Files]

**Output Format:** [PNG or JPEG images, video files, and ZIP archives containing GLB meshes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally under the configured output directory. The skill may request server-side deletion of this run's outputs and uploaded inputs after successful retrieval.]

## Skill Version(s):

4.7.2 (source: frontmatter, VERSION, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
