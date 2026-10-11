## Description:

Helps create Seedance 2.0 videos from text prompts, reference media, or first and last frames through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request videos from text, image, video, and audio references, or specified first and last frames. It provides commands for generating and retrieving results through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image, video, or audio files are sent to dLazy's hosted service.

Mitigation: Only submit prompts and media that you intend to share with dLazy.

Risk: The CLI can store an API key locally, and installing its package adds a supply-chain dependency.

Mitigation: Review the pinned CLI package before installation; use DLAZY_API_KEY for temporary access if you do not want to save a key locally.

## Reference(s):

- [dLazy CLI source (listed in skill metadata; release import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be returned as hosted URLs or saved locally on request.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
