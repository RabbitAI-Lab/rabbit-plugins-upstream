## Description:

Detect whether an image, video, or audio file may be AI-generated, including possible deepfakes, and return confidence scores and likely generator attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media reviewers use this skill to assess images, videos, or audio for AI generation, possible face swaps, and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media may be uploaded to dLazy storage and shared with dLazy and its analysis provider.

Mitigation: Submit only media you intend to share with those services, and review the provider's privacy terms first.

Risk: Using the analysis service may consume paid credits, and signing in stores an API key in the local CLI configuration.

Mitigation: Check costs before analysis and protect the local configuration that contains the API key.

Risk: Detection confidence scores are estimates and do not prove that media is AI-generated or a deepfake.

Mitigation: Treat scores as one signal and seek corroboration before making consequential decisions.

## Reference(s):

- [CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON results with a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence scores, AI-generation and deepfake indicators, and likely generator attribution; scores are estimates.]

## Skill Version(s):

1.0.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
