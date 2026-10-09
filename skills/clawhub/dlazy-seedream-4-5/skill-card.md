## Description:

Generates images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts or transform reference images with Seedream 4.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference media are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive content without approval for third-party processing.

Risk: Login may save an API key under the user's profile.

Mitigation: Use DLAZY_API_KEY when local key persistence is undesirable, and protect or revoke stored keys as needed.

Risk: Global installation runs a third-party CLI package.

Mitigation: Review the pinned npm package before installation; consider the documented npx alternative.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (metadata link, not release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, JSON task status]

**Output Format:** [JSON response with image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2k or 4k resolution and asynchronous generation.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
