## Description:

抖音短视频一站式解析与创作工场：用户提供抖音视频链接和需求后，技能通过 Cue Omni Reader 远程端点解析视频，再生成转录稿、内容总结、爆款拆解、分镜脚本、原创脚本或提示词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and content teams use this skill to turn Douyin video links into readable transcripts, summaries, content breakdowns, reusable script structures, new short-video scripts, and generation prompts. The skill is intended for content analysis and creation workflows that can tolerate third-party remote parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided Douyin links to Cue's remote parsing service and requires a Cue API key.

Mitigation: Tell users before parsing that links are sent to the Cue remote endpoint, use the documented no-store setting when available, and prefer the CUE_API_KEY environment variable over storing credentials in ~/.cue/config.json.

Risk: The security review flags promotional behavior around insufficient credits, including referral and paid subscription prompts.

Mitigation: Keep credit guidance brief and factual, make clear that parsing did not start, and avoid pressuring the user toward referral or payment options.

Risk: Visual recognition can misidentify people, works, or scenes, especially for film and television commentary videos.

Mitigation: Base factual claims on speech transcripts when possible, mark visual descriptions and shot details as inferred, and warn readers when screen analysis may be wrong.

Risk: Generated breakdowns or scripts may encourage copying copyrighted or platform-restricted content.

Mitigation: Frame analysis as structural learning, avoid helping users bypass copyright or platform controls, and remind users to obtain rights for commercial reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/douyin-video-studio)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue subscription page](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, transcripts, generated scripts, prompt text, optional JSON snippets, and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write generated Markdown reports to the workspace using video-specific filenames; includes warnings for inferred visual details and possible recognition errors.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
