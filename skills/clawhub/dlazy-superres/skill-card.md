## Description:

Helps agents upscale low-resolution images with dLazy and return a link to the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to improve the clarity of low-resolution images and retrieve the enhanced image URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media is uploaded to dLazy, and supplied parameters are sent to its hosted service.

Mitigation: Use only images and inputs approved for dLazy's hosted service; review what will be sent before running the skill.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Protect the local config, or supply the key per invocation; rotate or revoke it if exposed.

Risk: Running the CLI installs or executes third-party software.

Mitigation: Review the CLI before use and prefer the pinned on-demand npx command if a persistent global installation is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance and CLI JSON containing an enhanced image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
