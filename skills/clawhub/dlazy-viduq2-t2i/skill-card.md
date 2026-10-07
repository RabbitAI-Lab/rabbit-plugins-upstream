## Description:

Generates images from text prompts or reference images using Vidu Q2 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request Vidu Q2 image generation from prompts or reference images and retrieve generated image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied for generation are sent to dLazy.

Mitigation: Share only prompts and media approved for the cloud service.

Risk: Installing a third-party CLI runs external code.

Mitigation: Review the pinned CLI and prefer on-demand execution when appropriate.

Risk: The CLI saves an API key in local configuration.

Mitigation: Protect the key as a credential and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and JSON image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs; the CLI can optionally save assets locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
