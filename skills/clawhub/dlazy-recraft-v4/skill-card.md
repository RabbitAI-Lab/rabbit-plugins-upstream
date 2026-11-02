## Description:

Generate 1MP raster images with refined design judgment for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals and developers can generate 1MP raster images from prompts, choose an aspect ratio, and optionally save results locally using dLazy Recraft V4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service, and media files may be uploaded for processing.

Mitigation: Send only prompts and media you are comfortable sharing with the service, and install the CLI only if you trust dLazy.

Risk: Login stores an API key in the local dLazy configuration, and placing a key directly in a command can expose it in shell history.

Mitigation: Prefer device-code login or the DLAZY_API_KEY environment variable; protect the local config and rotate or revoke the key if exposed.

Risk: Image generation can consume account credits.

Mitigation: Use --dry-run to review the estimated cost before submitting a generation request.

## Reference(s):

- [dLazy CLI project page (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Files]

**Output Format:** [JSON result containing generated image URLs; optionally saved raster image files]

**Output Parameters:** [Prompt and optional aspect ratio; optional async mode and local save path]

**Other Properties Related to Output:** [Generated raster images are up to 1 MP. Async requests can initially return a task identifier without image outputs.]

## Skill Version(s):

1.3.36 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
