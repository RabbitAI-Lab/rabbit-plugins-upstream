## Description:

Detect whether an image, video, or audio file is AI-generated, identify possible visual deepfakes and likely generators, and return confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can submit image, video, or audio media to check for AI generation, possible face swaps, and likely generators. The result provides confidence scores and a structured verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media may be uploaded to an external service for analysis, and using the service may incur charges.

Mitigation: Submit only media you intend to send to the service, and review applicable service costs before running detection.

Risk: The partial scan flagged broad triggering and a mismatch between the advertised detection purpose and inspected login commands; the executable's behavior was not established.

Mitigation: Review the requested action and the installed CLI behavior before use, and invoke detection only for a specific image, video, or audio input.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON verdict with confidence scores and a human-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include media type, AI-generation and deepfake indicators, likely generator, and asynchronous task status; text input is not supported.]

## Skill Version(s):

1.0.42 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
