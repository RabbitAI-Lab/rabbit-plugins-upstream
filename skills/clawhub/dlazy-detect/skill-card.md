## Description:

Detects likely AI-generated images, videos, and audio, including visual deepfakes and possible generator models, with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can check images, videos, or audio for signs of AI generation, deepfakes, and possible generator models using confidence scores. Text detection is not supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or audio may be uploaded to dLazy's hosted service.

Mitigation: Confirm the selected file or URL and obtain permission before submitting private media.

Risk: A dLazy API key is stored locally for authenticated requests.

Mitigation: Protect the local credential and use the CLI's supported authentication options.

Risk: Broad trigger words can cause unintended requests that consume API quota.

Mitigation: Confirm the intended media and request before invoking detection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [JSON verdict with confidence scores and a plain-text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A detection result may include deepfake and likely-generator scores; asynchronous requests return a task identifier until complete.]

## Skill Version(s):

1.0.24 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
