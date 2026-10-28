## Description:

Detects whether image, video, or audio media is AI-generated and returns confidence scores, deepfake results, and likely generator attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can check image, video, or audio media for signs of AI generation, visual deepfakes, and likely generator models. They can use the returned confidence scores to inform their review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files are uploaded to dLazy media storage for remote analysis, and the service may consume paid credits.

Mitigation: Only submit media you are comfortable sharing with dLazy and its analysis provider. Use the documented dry-run option to review the payload and cost estimate before making a request.

Risk: CLI authentication can save the API key in the local user configuration file.

Mitigation: Protect the saved key; use the documented DLAZY_API_KEY environment variable when you want to avoid saving it through CLI authentication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key instructions](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured JSON results with a human-readable text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confidence scores for AI generation and deepfake detection, with likely generator attribution where available. Supports image, video, and audio media; text is unsupported.]

## Skill Version(s):

1.0.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
