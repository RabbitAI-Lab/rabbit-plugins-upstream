## Description:

Guides an agent in generating and editing images, animating images into video, and creating 3D meshes through a user-configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ComfyUI users can ask an agent to create or edit images, extract subjects onto transparent backgrounds, turn images into videos, or package character meshes for delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, workflow data, source images, and any configured API key are sent to the selected ComfyUI server.

Mitigation: Use a server you control or trust, prefer localhost or trusted HTTPS, and avoid sensitive inputs unless its handling is acceptable.

Risk: Generated media may be stored in local output or delivery locations.

Mitigation: Check the configured output location before processing sensitive media.

## Reference(s):

- [Publisher profile](https://clawhub.ai/user/sunshinejnjn)
- [ComfyUI skill setup and usage](artifact/README.md)
- [Model download sources](artifact/MODEL_URL.txt)
- [Workflow source attribution](artifact/references/attribution.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Generated media files]

**Output Format:** [Text guidance and attached JPG or PNG images, video files, or ZIP archives containing GLB meshes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transparent image cutouts require PNG; 3D meshes are delivered as ZIP archives.]

## Skill Version(s):

3.6.0 (source: ClawHub release metadata; bundled frontmatter says 3.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
