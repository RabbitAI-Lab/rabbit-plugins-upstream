## Description:

Generates and edits images, creates short videos, extracts transparent-background cutouts, and creates 3D meshes through a configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers and other ComfyUI users use the skill to generate or edit images, create short videos, extract image subjects, and produce 3D meshes from prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hunyuan 3D runs may remove uploaded source copies and cutouts before mesh completion, leaving no server-side recovery copy if the final mesh fails.

Mitigation: Until cleanup waits for complete job success, use `--keep` or set `COMFYUI_PURGE=0`, and keep local originals.

Risk: Prompts and uploaded images are sent to the configured ComfyUI server, and external server plugins were not bundled or exercised.

Mitigation: For remote servers, use a trusted HTTPS endpoint and avoid sending sensitive inputs unless its handling is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [Output delivery guidance](artifact/references/delivery.md)
- [ComfyUI authentication plugin reference](https://github.com/sunshinejnjn/comfyui-auth)
- [ComfyUI purge plugin reference](https://github.com/sunshinejnjn/comfyui-purge-after-retrieval)

## Skill Output:

**Output Type(s):** [Image files, Video files, 3D mesh files]

**Output Format:** [JPEG or PNG images, video files, and GLB meshes packaged as ZIP files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved under the configured output directory; deliverables vary by generation mode.]

## Skill Version(s):

4.7.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
