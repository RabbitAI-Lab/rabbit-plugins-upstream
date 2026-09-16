## Description:

B站视频全解析 helps agents turn Bilibili video URLs into transcripts, summaries, content breakdowns, scripts, prompts, PPT extraction, and study notes using Cue Omni Reader parsing plus model-assisted transformation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, and learning teams use this skill to convert Bilibili video URLs into reusable Markdown reports, scripts, prompts, course notes, or exam study notes. The skill is also useful for agents that need structured video-derived content while preserving source timestamps where available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may promote Cue referral or payment links when handling credit errors.

Mitigation: Review and edit the credit-error guidance before installation if promotional referral or payment messaging is not acceptable.

Risk: The skill can send supplied Bilibili URLs to Cue remote parsing services and may query Bilibili APIs in fallback flows.

Mitigation: Use it only for videos that are acceptable to send to those services, and inform users before remote parsing begins.

Risk: The artifact includes local API-key configuration as an option, which can leave credentials in a user home directory.

Mitigation: Prefer supplying CUE_API_KEY as a runtime environment variable instead of writing the key to ~/.cue/config.json.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/bilibili-video-studio)
- [Cue Omni Reader hub](https://cuecue.cn/hub/omni-reader)
- [Cue API key management](https://cuecue.cn/hub/api-key)
- [Cue Omni Reader remote endpoint](https://mcp.cuecue.cn/api/omni-reader/mcp/)
- [Bilibili video metadata API](https://api.bilibili.com/x/web-interface/view?bvid=BVxxxxxxxx)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, code blocks, and optional structured JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write scenario-specific Markdown files named for the Bilibili video ID and requested task.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
