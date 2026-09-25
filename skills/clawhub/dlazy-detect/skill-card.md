## Description:

Detects whether image, video, or audio media is AI-generated, including visual deepfake signals and likely generator attribution, and returns confidence scores for thresholding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy media detection on a single image, video, or audio input and return AI-generation, deepfake, and likely-generator confidence signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media submitted for analysis may be uploaded to dLazy storage and processed by dLazy's hosted service.

Mitigation: Use the skill only for media that is appropriate to send to dLazy, and avoid private, confidential, or biometric media unless that service use is acceptable.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication when a persistent local credential is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task status when invoked with no-wait mode.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
