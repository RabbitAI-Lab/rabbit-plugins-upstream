## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5. 使用即梦 (Jimeng) OmniHuman 1.5 模型，通过人像图片和音频/文本生成逼真的数字人播报视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate digital human broadcast videos from a portrait image and audio or text prompt using Jimeng OmniHuman 1.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portrait images and audio or video files supplied through local paths are uploaded to dLazy media storage, and prompts are sent to its hosted API.

Mitigation: Submit only media and prompts that are appropriate to share with the service, and use portrait likenesses with the subject's permission.

Risk: The supplied security review has medium confidence and partial coverage because some local references could not be resolved; it also notes a low-probability whitespace-padding alert.

Mitigation: Review the unresolved local references and flagged whitespace area before installing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video asset with JSON result metadata and a hosted result URL; the asset can also be saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 720p and 1080p output; asynchronous requests can return a task ID for later status checks.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
