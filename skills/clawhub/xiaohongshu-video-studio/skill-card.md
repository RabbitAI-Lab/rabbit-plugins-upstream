## Description:

小红书短视频全解析 helps an agent parse Xiaohongshu video links through Cue Omni Reader and produce transcripts, summaries, viral-content breakdowns, shooting scripts, rewritten scripts, and generation prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content agents use this skill to turn Xiaohongshu video links into reusable transcripts, summaries, content analysis, scripts, and prompts. It is aimed at video understanding and short-form content production workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer users toward provider referral or payment flows when Cue credits are insufficient.

Mitigation: Review the skill before installation and decide whether referral or payment prompts are acceptable in the target agent experience.

Risk: Xiaohongshu video links and the Cue API key are used with the Cue remote parsing service.

Mitigation: Use an environment variable such as CUE_API_KEY for the key, avoid plaintext local config unless accepted, and disclose remote parsing to users.

Risk: Content breakdowns and rewrite workflows can be used too closely to imitate source videos.

Mitigation: Use outputs for analysis and structural inspiration, and review copyright, platform, and advertising-law constraints before publishing derivative scripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/xiaohongshu-video-studio)
- [Cue Omni Reader Online Experience](https://cuecue.cn/hub/omni-reader)
- [Cue API Key Management](https://cuecue.cn/hub/api-key)
- [Cue Omni Reader Remote MCP Endpoint](https://mcp.cuecue.cn/api/omni-reader/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, structured JSON snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include timestamped transcripts, timeline tables, score reports, rewritten scripts, prompt JSON, and Cue API configuration guidance.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
