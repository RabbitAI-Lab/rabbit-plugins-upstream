## Description:

Analyzes local or remote video with Alibaba Cloud Qwen 3.5 Plus, allowing a custom prompt and frame-sampling FPS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fackee](https://clawhub.ai/user/fackee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to summarize videos, describe scenes, identify actions or objects, and produce analysis text from a local video file or publicly accessible video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled local agent permissions preapprove broad Python and chmod shell commands.

Mitigation: Review before installing and remove or narrow the .claude permissions, especially Bash(python3:*) and Bash(chmod:*).

Risk: The DashScope dependency is unpinned.

Mitigation: Pin dashscope to a reviewed version before deployment.

Risk: Video content is submitted to Alibaba Cloud Qwen/DashScope for analysis.

Mitigation: Only submit videos you are allowed to send to that service and review data-handling requirements for the intended use case.

Risk: The skill depends on a local DashScope API key.

Mitigation: Protect the API key in ~/.openclaw/openclaw.json and avoid sharing logs or screenshots that include it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fackee/skills/analyze-video-by-qwen)
- [DashScope API endpoint used by the skill](https://dashscope.aliyuncs.com/api/v1)
- [DashScope US regional endpoint noted by the skill](https://dashscope-us.aliyuncs.com/api/v1)
- [DashScope international regional endpoint noted by the skill](https://dashscope-intl.aliyuncs.com/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text analysis printed to the terminal, with Markdown usage examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DashScope API key in ~/.openclaw/openclaw.json; higher FPS settings can increase API cost.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
