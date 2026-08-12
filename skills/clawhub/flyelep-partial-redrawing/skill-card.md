## Description:

Uses the Flyelep AI Tool API to redraw part of an image from a source image URL, a text prompt, and an optional reference image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image-editing agents use this skill when a user wants to partially modify an image, replace a background or region, or preserve the main subject while changing specific content through Flyelep's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends image URLs, the editing prompt, an optional reference image URL, and the Flyelep API key to Flyelep.

Mitigation: Use runtime-only key entry, avoid sensitive or private image content unless Flyelep is acceptable for that data, and delete temporary payload files after use.

Risk: A vague editing prompt can produce an unintended redraw or alter more of the image than the user expects.

Mitigation: Ask the user to specify what to change, what to preserve, and whether a reference image should be used before calling the API.

## Reference(s):

- [Flyelep partial redrawing API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/partialRedrawing)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-partial-redrawing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Text]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands; runtime API response is JSON containing the redrawn image URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided source image URL, text prompt, optional reference image URL, and runtime Flyelep API key.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
