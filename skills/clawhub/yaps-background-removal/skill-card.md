## Description:

Remove an image background with Yaps. Save a transparent PNG, solid background, or outlined sticker. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to remove backgrounds from local JPG, PNG, WebP, or BMP images with the Yaps desktop engine and save a new PNG as a transparent cutout, solid-background image, or outlined sticker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled runtime exposes broader Yaps command passthrough, transcription, and meeting workflows beyond background removal.

Mitigation: Review the package before installing, use only the documented media remove-background workflow for this skill, and inspect command help before enabling additional Yaps capabilities.

Risk: The skill operates on local files and the user's local Yaps account session.

Mitigation: Use exact requested input files, save to new output paths, preserve originals, and avoid unrequested hosted image APIs or other upload fallbacks.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-background-removal)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with CLI commands and generated PNG file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a new PNG output; supported modes include transparent background, solid color background, and outlined sticker.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
