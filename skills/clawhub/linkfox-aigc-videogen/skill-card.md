## Description:

AIGC视频生成 generates short videos from a starting image, optional ending frame, prompt, and selected LinkFox-supported video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit image-to-video generation jobs through LinkFox APIs, select supported model settings, and retrieve generated local video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs, prompts, task metadata, and the LinkFox API key are sent to LinkFox-controlled services.

Mitigation: Use only media and prompts approved for third-party processing, and configure credentials intentionally.

Risk: Video generation may consume LinkFox credits or quota.

Mitigation: Confirm generation requests before execution and monitor account balance or quota before repeated use.

Risk: During authentication or billing failures, the skill may ask to download and install a separate onboarding skill from a remote URL.

Mitigation: Require explicit user approval and review the downloaded onboarding skill before installation.

Risk: Generated videos and fallback API responses are stored locally in session directories.

Mitigation: Handle saved media and response files according to the sensitivity of the source images and prompts.

## Reference(s):

- [AI 生视频 API 参考（首尾帧/单图模式）](references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen)
- [LinkFox API key and credits guide](https://skill.linkfox.com/linkfoxskills/guide.htm)

## Skill Output:

**Output Type(s):** [text, shell commands, files, guidance]

**Output Format:** [Plain text or Markdown status with local video file paths; JSON parameters are passed to the Python script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are saved to the session media directory; raw API responses are saved to the session data directory when no video file is produced.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
