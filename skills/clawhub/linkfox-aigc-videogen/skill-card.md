## Description:

AI生视频工具（首尾帧/单图模式），根据原图和提示词生成视频，支持可选尾帧图控制结束画面，支持 KLING、WAN、SEED、SEED_FAST 和 HAILUO 模型。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short AI videos from a source image, optional ending frame, and prompt through LinkFox video-generation services. It also guides users through API-key setup and billing recovery when authentication or balance errors block generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends generation requests and account-recovery actions to LinkFox network services, including API-key setup and payment-order creation when auth or billing errors occur.

Mitigation: Install only if those network and account flows are acceptable; prefer LinkFox self-service account and billing pages when possible, and review payment QR codes and shell-profile commands before using them.

Risk: API keys and phone/SMS login details may be exposed or persisted if configured on a shared machine.

Mitigation: Avoid storing API keys permanently on shared systems, keep credentials out of transcripts and logs, and remove or rotate environment variables when access is no longer needed.

Risk: Generated media may involve signed or temporary URLs and large local files.

Mitigation: Share only the downloaded local media path with the user, do not read video file contents or expose base64 media, and avoid publishing raw temporary API URLs.

## Reference(s):

- [AI 生视频 API 参考（首尾帧/单图模式）](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen)
- [LinkFox self-service site](https://agent.linkfox.com/)
- [LinkFox tool gateway](https://tool-gateway.linkfox.com)
- [LinkFox feedback API](https://skill-api.linkfox.com/api/v1/public/feedback)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, local media file paths, and generated video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates asynchronous LinkFox API tasks, polls for completion for up to 20 minutes, saves generated videos under a session media directory, and writes raw API responses under data only for troubleshooting.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
