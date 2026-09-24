## Description:

Create an image from a written prompt with Yaps. Save the result or make a sticker. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to create PNG images from text prompts through a local Yaps desktop installation, with optional sticker output when the required dependency is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is framed as image generation, but the bundled runner can expose broader Yaps media and meeting workflows.

Mitigation: Review the installed skill before use and keep execution limited to user-requested image generation unless broader local Yaps automation is acceptable.

Risk: The runner can process local audio, video, meeting, and image files through the desktop Yaps account.

Mitigation: Keep file selection user-directed, use new output paths, and avoid sending source files to other services as an unrequested fallback.

Risk: Model downloads, feature availability, and sticker output depend on local Yaps capabilities and dependencies.

Mitigation: Check feature readiness and command help first, describe any reported model download size, and obtain authorization before enabling downloads.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [Yaps Image Generate on ClawHub](https://clawhub.ai/yaps/skills/yaps-image-generate)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated PNG file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation depends on a reachable local Yaps desktop installation, supported hardware, signed-in account access, and available image-generation features.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
