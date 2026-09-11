## Description:

抖音短视频一站式解析与创作工场：用户提供抖音视频链接和需求后，技能通过 Cue Omni Reader 远程解析并生成转录、摘要、爆款拆解、分镜脚本、原创脚本或提示词反推结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to turn Douyin video links into transcripts, structured summaries, growth analysis, reusable script outlines, new short-video scripts, and generation prompts. The skill is intended for agent-assisted content analysis and production workflows where users supply the video link and review the generated output before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Douyin links and parsed content are sent to Cue's remote service.

Mitigation: Use only for content the user is comfortable transmitting to Cue; avoid private, sensitive, copyrighted, or unauthorized material.

Risk: Cue API keys may be exposed if stored directly in local files or shared commands.

Mitigation: Prefer the CUE_API_KEY environment variable and avoid writing API keys into durable local configuration unless the user explicitly accepts that storage.

Risk: Video frame interpretation can misidentify people, works, or scenes, especially for film and drama commentary.

Mitigation: Treat spoken transcript and parsed timestamps as the primary evidence, and label inferred visual conclusions before using them in reports or scripts.

Risk: Generated teardown or script output can create copyright, platform-rule, or advertising-compliance issues if reused without review.

Mitigation: Use the output as draft guidance, require human review for rights and factual claims, and avoid assisting with copying protected content or bypassing platform restrictions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/douyin-video-studio)
- [Cue Omni Reader Hub](https://cuecue.cn/hub/omni-reader)
- [Cue API Key Management](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, optional JSON prompt structures, and inline shell or Python snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write Markdown deliverables named from the video identifier and selected scenario; generated analysis should distinguish parsed content from model-inferred shots, camera movement, transitions, or emotion.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
