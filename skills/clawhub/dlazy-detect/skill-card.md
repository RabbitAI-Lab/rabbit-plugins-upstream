## Description:

Helps detect AI-generated images, video, and audio, including visual deepfakes and likely generator models, with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can check images, video, or audio for signs of AI generation and review confidence scores, potential deepfakes, and likely generator models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, video, and audio submitted for detection are uploaded to dLazy infrastructure.

Mitigation: Use non-sensitive test media or public URLs where possible, and confirm that media may be shared before submitting it.

Risk: Authentication may store a dLazy API key in a local configuration file.

Mitigation: Protect the local credential file and avoid sharing the API key in prompts or outputs.

Risk: Broad trigger terms can cause unintended invocation.

Mitigation: Confirm the user intends to analyze the selected media before running detection.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Human-readable summary and structured JSON verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence scores for AI generation and, where applicable, deepfakes and likely generator models; does not analyze text.]

## Skill Version(s):

1.0.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
