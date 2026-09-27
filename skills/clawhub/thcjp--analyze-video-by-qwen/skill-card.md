## Description:

Qwen视频智能分析 helps agents analyze local video files or public video URLs with Qwen 3.5 Plus, using configurable prompts and frame-sampling FPS for scene description, object and action recognition, summarization, content review, and video Q&A.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, media asset managers, educators, and operations reviewers use this skill to ask an agent for video understanding over local files or public URLs. Typical tasks include generating scene summaries, identifying objects or actions, reviewing content, and answering focused questions about a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send local media or public video URLs to Alibaba Cloud DashScope/Qwen for analysis.

Mitigation: Use only media you are allowed to process with that provider and review third-party data terms before using sensitive or regulated video.

Risk: The release evidence reports unclear third-party data disclosure for a cloud video-analysis workflow.

Mitigation: Document the provider interaction for users and require a review step before applying the skill to confidential or regulated content.

Risk: API-key instructions are inconsistent across the artifact and may lead users to store credentials in the wrong location.

Mitigation: Standardize on one protected configuration path and avoid displaying, echoing, or accepting API keys in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analyze-video-by-qwen)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and text analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses video_source, fps, and prompt; higher FPS can increase API calls and cost.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
