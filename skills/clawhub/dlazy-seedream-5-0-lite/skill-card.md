## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image generation or image-to-image transformations from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected local media may be sent to the third-party dLazy service.

Mitigation: Confirm the user's intent and review prompts and selected files before uploading sensitive content.

Risk: The CLI may store a revocable API key on the user's device.

Mitigation: Keep the key private and rotate or revoke it if exposure is suspected.

Risk: Generic image-generation requests may unintentionally trigger a third-party service call.

Mitigation: Ask for clear user intent before invoking this skill for an ambiguous request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and can optionally be saved locally.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence; bundled skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
