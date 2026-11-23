## Description:

Generates short text-to-video and image-to-video clips with Google Veo 3.1 Fast. 使用 Google Veo 3.1 Fast 极速版模型，快速响应并生成短时长的文生视频或图生视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can generate short videos from text prompts or supplied frames, and extend an existing video. The skill supports common video sizes and resolutions and returns generated output for the agent to share or save.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security scan did not resolve several references or verify the CLI package’s behavior.

Mitigation: Review the CLI package and relevant service documentation before installing or using the skill.

Risk: Prompts and supplied local media are sent to dLazy hosted services for generation.

Mitigation: Avoid sending sensitive prompts or media unless you are authorized to share them, and review dLazy’s service terms.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may be asynchronous; the result can include a task identifier for later status checks.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
