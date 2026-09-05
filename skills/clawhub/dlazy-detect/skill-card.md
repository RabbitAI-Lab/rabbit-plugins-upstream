## Description:

Detect whether an image, video, or audio file is AI-generated, including visual deepfakes and likely generator models, and return confidence scores for thresholding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to check images, video, or audio for AI generation, deepfakes, and likely generator attribution through the dLazy CLI/API. It is suited for media review workflows where confidence scores can guide downstream human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media may be uploaded to dLazy remote storage/API for analysis.

Mitigation: Use the skill only with media the user explicitly intends to submit, and avoid confidential, private, or regulated files unless the user has approved that upload.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, use a narrowly scoped key where available, and remove or rotate the key when access is no longer needed.

Risk: The trigger scope is broad enough that an agent could invoke detection on unintended media.

Mitigation: Prefer explicit invocations such as 'dlazy detect' with a clearly intended media file and confirm ambiguous media-selection requests before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON detection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one media input flag per detection request; local media may be uploaded to dLazy-hosted storage/API.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
