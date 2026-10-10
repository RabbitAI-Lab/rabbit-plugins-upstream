## Description:

Analyzes a reference image's composition, colors, lighting, and style to guide generation of a similar-style image with Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate new images in the style of a reference image through the dLazy image-replication service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be stored in the local dLazy configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when persistence is unnecessary, and rotate or revoke keys if needed.

Risk: Selected prompts and images are sent to dLazy's cloud service.

Mitigation: Review selected content and confirm cloud upload is acceptable before invoking the skill.

Risk: Image-generation requests may use paid credits.

Mitigation: Check the available credits and use the CLI's dry-run cost estimate before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and image-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns image URLs or an asynchronous task ID; results can optionally be saved to a local file.]

## Skill Version(s):

1.3.28 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
