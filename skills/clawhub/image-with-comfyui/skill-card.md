## Description:

Generate, edit, or animate images and videos, create transparent-background cutouts, and turn images into 3D meshes through a configured ComfyUI server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

BSD 3-Clause

## Use Case:

Developers and other agent users can generate or edit images, create short videos, extract transparent-background subjects, and generate 3D meshes by sending prompts and, where needed, source images to their configured ComfyUI server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video cleanup and download-validation defects may leave private media on the server or delete server copies after a failed download.

Mitigation: Avoid sensitive images, use --keep, verify downloaded videos, and manage server cleanup manually until these defects are fixed.

Risk: Prompts and source images are sent to the configured ComfyUI endpoint, and generated media is written to the configured output directory.

Mitigation: Use a trusted server with HTTPS and server-side authentication for remote connections, and review the endpoint and output location before sending sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui)
- [README.md](README.md)
- [CLI reference](references/cli-reference.md)
- [Prompt guidance](references/prompts.md)
- [Delivery guidance](references/delivery.md)
- [Error handling](references/error-handling.md)
- [Model sources](MODEL_URL.txt)
- [ComfyUI authentication reference implementation](https://github.com/sunshinejnjn/comfyui-auth)
- [ComfyUI retrieve-then-purge plugin](https://github.com/sunshinejnjn/comfyui-purge-after-retrieval)

## Skill Output:

**Output Type(s):** [Image files, Video files, 3D mesh archives]

**Output Format:** [PNG or JPEG images, generated video files, and ZIP archives containing GLB meshes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to the configured output directory and the script reports local output paths.]

## Skill Version(s):

4.5.7 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
