## Description:

Detects whether images, videos, or audio are AI-generated and reports deepfake likelihood, likely generator, and confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to assess whether an image, video, or audio file is AI-generated, check visual deepfake likelihood, and review confidence scores and likely generator attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files are uploaded to dLazy media storage for analysis, and scanner coverage could not establish the CLI’s internal authentication behavior.

Mitigation: Only submit media approved for external processing, and confirm the CLI login flow and service fit your security requirements before connecting an account.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON verdict with a concise human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns media type, AI-generation and deepfake scores, boolean classifications, and likely generator attribution where available; text input is unsupported.]

## Skill Version(s):

1.0.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
