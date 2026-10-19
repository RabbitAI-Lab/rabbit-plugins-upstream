## Description:

Checks images, videos, and audio for signs of AI generation, including visual deepfakes and likely generator attribution, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can assess whether an image, video, or audio clip may be AI-generated and review confidence scores, possible deepfakes, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio files submitted for detection are uploaded to dLazy's hosted service.

Mitigation: Submit only media you are comfortable sharing; prefer public URLs or non-sensitive local files.

Risk: The CLI can persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if you do not want the key saved locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON detection verdict with a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence scores and possible generator attribution; asynchronous requests can return a task ID instead of a verdict.]

## Skill Version(s):

1.0.30 (source: ClawHub release metadata; skill frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
