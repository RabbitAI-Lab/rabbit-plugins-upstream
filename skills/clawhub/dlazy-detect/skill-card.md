## Description:

Detects whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator models, and returns confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to assess whether an image, video, or audio file is AI-generated, estimate deepfake likelihood, and review confidence scores and likely image or video generators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and was partial; it could not verify how login supports the advertised detection feature.

Mitigation: Review the authentication flow and API key requirements before installing or using the skill.

Risk: Local media files are uploaded to dLazy storage for analysis.

Mitigation: Submit only media you are authorized to share and comfortable sending to the service.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON with a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one image, video, or audio input per detection; text input is not supported. Returns confidence scores and, for images or video, a likely generator when available.]

## Skill Version(s):

1.0.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
