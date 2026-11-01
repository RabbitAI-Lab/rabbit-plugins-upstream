## Description:

Generates, edits, and animates images and creates 3D meshes through a configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate or edit images, animate images into videos, and create 3D meshes from images through their configured ComfyUI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One 3D mode may delete server-side copies before the generation job succeeds.

Mitigation: Use --keep or COMFYUI_PURGE=0, especially with hyi2m, until cleanup waits for the full pipeline to succeed; keep local originals.

Risk: Prompts and selected images are sent to the configured ComfyUI endpoint.

Mitigation: Choose an endpoint you trust and use HTTPS when connecting remotely.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [CLI reference](references/cli-reference.md)
- [Error handling](references/error-handling.md)
- [Output delivery](references/delivery.md)
- [Prompt guidance](references/prompts.md)

## Skill Output:

**Output Type(s):** [Images, Video, 3D mesh files]

**Output Format:** [JPG or PNG images, video files, and GLB meshes packaged in ZIP files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally; 3D mesh delivery uses ZIP packages.]

## Skill Version(s):

4.6.9 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
