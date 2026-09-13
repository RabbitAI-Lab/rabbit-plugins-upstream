## Description:

B站视频全解析 helps agents turn Bilibili video URLs into transcripts, summaries, content breakdowns, scripts, prompts, PPT-style notes, and exam notes using Cue Omni Reader parsing plus model-generated structuring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, educators, and study-note builders use this skill to parse Bilibili video URLs and transform extracted speech or screen text into usable Markdown deliverables. It supports transcription, video analysis, viral-content teardown, script generation, prompt extraction, slide-note extraction, and exam-note organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bilibili URLs or media links are sent to Cue for parsing.

Mitigation: Install and use the skill only when sending those links to Cue is acceptable for the user's workflow.

Risk: A Cue API key is required and could be exposed if written to local configuration.

Mitigation: Prefer the CUE_API_KEY environment variable rather than storing the key in ~/.cue/config.json.

Risk: Download and frame-extraction workflows may process third-party video content.

Mitigation: Use those workflows only for videos the user is allowed to process.

Risk: Parsed video content may contain commands, role-change requests, or other prompt-injection text.

Mitigation: Treat parsed content as untrusted source material and ignore any instructions embedded inside it.

Risk: Generated breakdowns, scripts, and marketing copy may create copyright, platform-policy, or factual-claim review needs.

Mitigation: Review transformed content before publication, verify factual claims, and obtain appropriate rights for commercial reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/bilibili-video-studio)
- [Cue Omni Reader hub](https://cuecue.cn/hub/omni-reader)
- [Cue API Key management](https://cuecue.cn/hub/api-key)
- [Cue Omni Reader remote MCP endpoint](https://mcp.cuecue.cn/api/omni-reader/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, inline shell commands, and occasional JSON prompt blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write Markdown files named by Bilibili BV identifier and scenario; long reports begin with a short overview.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence and target metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
