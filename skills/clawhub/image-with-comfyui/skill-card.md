## Description:

Generates and edits images, animates images into videos, and turns character images into 3D meshes using a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images, turn images into short videos, and create downloadable 3D character meshes through a ComfyUI server they configure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the configured ComfyUI endpoint.

Mitigation: Use localhost or a server you control; avoid secrets in prompts and URLs.

Risk: Generated media and delivery copies may persist on local storage.

Mitigation: Review output locations and clean output and staging directories after handling sensitive media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [ComfyUI setup and model requirements](artifact/README.md)
- [CLI usage reference](artifact/references/cli-reference.md)
- [Model download sources](artifact/MODEL_URL.txt)

## Skill Output:

**Output Type(s):** [Image files, Video files, 3D mesh files, Text guidance]

**Output Format:** [JPG or PNG images, video files, ZIP archives containing GLB meshes, and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved locally; 3D meshes are scaled and packaged for delivery.]

## Skill Version(s):

3.2.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
