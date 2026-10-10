## Description:

Generates images from text prompts or reference images using Kling Image O1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images using references through dLazy's hosted Kling Image O1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to dLazy, and generated assets are hosted on dLazy storage.

Mitigation: Confirm the user wants this provider and avoid sending sensitive prompts or media without approval.

Risk: Image generation consumes paid credits.

Mitigation: Confirm intended usage and review the estimated cost with the CLI's dry-run option before submitting requests.

Risk: Authentication can save a dLazy API key locally.

Mitigation: Protect local credentials; use a per-invocation key when persistent storage is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI repository linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, Image files, Text]

**Output Format:** [JSON result with hosted image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an image immediately.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; embedded skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
