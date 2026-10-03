## Description:

Helps detect AI-generated images, video, and audio, including visual deepfakes and likely generator models, with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can check images, video, or audio for signs of AI generation and review confidence scores, deepfake indicators, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media submitted for analysis may be uploaded to dLazy storage and processed by its hosted service.

Mitigation: Use public URLs or non-sensitive test media when privacy matters, and confirm permission before submitting sensitive media.

Risk: The CLI can save an API key in a local configuration file.

Mitigation: Use DLAZY_API_KEY for per-session authentication if you do not want a saved key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with detection summaries and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report AI-generation and deepfake confidence scores and a likely generator; text detection is not supported.]

## Skill Version(s):

1.0.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
