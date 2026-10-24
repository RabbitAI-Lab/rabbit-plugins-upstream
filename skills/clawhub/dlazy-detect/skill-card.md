## Description:

Detect whether an image, video, or audio file is AI-generated, including possible deepfakes, and report confidence scores and likely generator attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can assess user-selected images, videos, or audio for signs of AI generation or deepfake manipulation, then use the returned confidence scores and likely generator as decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is sent to dLazy's hosted detection service, which may be unsuitable for sensitive content.

Mitigation: Submit only media you are authorized to share, and review dLazy's privacy and retention terms before uploading sensitive files.

Risk: Using the service can incur charges, and the CLI stores an API key locally.

Mitigation: Confirm costs before submitting jobs and protect the saved API key.

Risk: Detection confidence scores are estimates and can be mistaken for definitive proof.

Mitigation: Treat results as decision support rather than proof, and seek corroborating evidence for consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON detection results with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes media type, AI-generation and deepfake confidence scores, and likely generator attribution when available.]

## Skill Version(s):

1.0.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
