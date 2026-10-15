## Description:

Generates short videos from text prompts or images using Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video generations, or extend a video, through dLazy's Veo 3.1 Fast service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service.

Mitigation: Upload only material you intend to share with dLazy.

Risk: The dLazy API key may be saved locally when logging in or setting authentication.

Mitigation: Protect the local credential and rotate or revoke it if compromised.

Risk: Video generation can consume dLazy credits.

Mitigation: Use the available dry-run option to check the payload and estimated cost before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands; JSON results with generated-media URLs or task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID for later status checks.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
