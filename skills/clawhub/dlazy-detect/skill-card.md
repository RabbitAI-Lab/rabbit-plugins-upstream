## Description:

Checks images, videos, or audio for AI generation, visual deepfakes, and likely generator models, returning confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can submit an image, video, or audio file to assess whether it may be AI-generated, whether a visual contains a deepfake, and which generator may have produced it. The skill returns confidence scores and a readable summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media submitted for analysis is shared with dLazy and its analysis provider; service charges and retention policies may apply.

Mitigation: Submit only media you are comfortable sharing, review applicable charges and retention policies, and protect the saved API key.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured JSON confidence scores with a short human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image and video results include AI-generation and deepfake scores; audio results include an AI-generated audio score.]

## Skill Version(s):

1.0.36 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
