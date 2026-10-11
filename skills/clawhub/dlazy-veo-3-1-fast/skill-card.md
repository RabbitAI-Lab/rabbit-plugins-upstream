## Description:

Guides agents in generating short text-to-video and image-to-video clips with Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in configuring and invoking dLazy's video-generation CLI for short clips from prompts or images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service.

Mitigation: Only submit prompts and media that you intend to share with dLazy.

Risk: The dLazy CLI can save an API key in local configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when you do not want a locally saved key.

Risk: Installing a third-party CLI introduces software supply-chain exposure.

Mitigation: Review the @dlazy/cli source and package before relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides CLI invocation; the dLazy service returns generation status and media URLs.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
