## Description:

Helps agents generate and edit images with Nano Banana 2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request new images or edits to supplied images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image paths or files are sent to dLazy-hosted services.

Mitigation: Confirm you trust the dLazy CLI and service before submitting sensitive prompts or images.

Risk: The CLI may save an API key locally and can be installed globally.

Mitigation: Protect the local API key and consider one-off npx use instead of a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI repository (tool linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON, Image files]

**Output Format:** [CLI commands and JSON results with image URLs; optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; results may be asynchronous.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
