## Description:

Generates 4MP raster images from text prompts for print-ready assets and large-format uses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and content creators use this skill to generate high-resolution images from prompts for print and large-format projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files supplied to the CLI are sent to dLazy's hosted service.

Mitigation: Review inputs and avoid sending sensitive prompts or files without approval.

Risk: The CLI can store an API key in the user's local configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication if persistent storage is unwanted; rotate or revoke keys in the dLazy dashboard when needed.

Risk: Installing the CLI runs a third-party npm package.

Mitigation: Review the pinned @dlazy/cli package before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source (linked in skill metadata; not verified as release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Image URLs]

**Output Format:** [JSON response with image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID for later retrieval.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
