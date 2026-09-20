## Description:

小红书短视频全解析把用户提供的小红书视频链接和需求转换为分段转录、内容总结、爆款拆解、分镜脚本、改写脚本和提示词，并通过 Cue Omni Reader 远程解析服务获取视频文本素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, and agent users use this skill to turn Xiaohongshu video links into transcripts, summaries, viral-video breakdowns, storyboard scripts, rewritten scripts, and generation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu video links, including access-bearing xsec_token values, are sent to Cue's remote parsing endpoint.

Mitigation: Use the skill only for links suitable for third-party processing, avoid private or sensitive videos, and disclose the remote transfer before parsing.

Risk: Cue API keys can be exposed if stored in plaintext configuration files or pasted into shared transcripts.

Mitigation: Prefer the CUE_API_KEY environment variable, do not commit keys, and avoid displaying secrets in agent output.

Risk: Generated transcripts, rewrites, and reusable script structures may raise copyright or platform-policy concerns when reused directly.

Mitigation: Review rights, attribution needs, and platform rules before publishing or commercializing derived content.

Risk: Storyboard fields such as camera movement, transitions, and emotion may be model inferences rather than parsed video facts.

Mitigation: Mark inferred fields clearly and keep factual claims grounded in parsed OCR, ASR, and timestamps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/xiaohongshu-video-studio)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue service](https://cuecue.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, optional structured JSON prompts, and inline shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include transcripts, summaries, scoring tables, storyboard scripts, rewritten scripts, prompt sequences, and saved Markdown files.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
