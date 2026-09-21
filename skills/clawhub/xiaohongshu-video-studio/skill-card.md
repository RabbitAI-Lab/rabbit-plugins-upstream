## Description:

小红书短视频全解析 helps agents turn Xiaohongshu video links into transcripts, summaries, virality breakdowns, shooting scripts, rewritten short-video scripts, and prompt drafts using Cue Omni Reader.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content operators use this skill to analyze Xiaohongshu videos and produce reusable Markdown deliverables such as transcripts, summaries, scoring reports, storyboard tables, rewritten scripts, and generation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu video links to Cue's remote service for parsing.

Mitigation: Review the data transfer before use and avoid submitting links that expose confidential, private, infringing, or platform-prohibited content.

Risk: The skill text tells users to paste a full Cue API key into chat so the agent can store it locally.

Mitigation: Configure CUE_API_KEY yourself or edit ~/.cue/config.json locally; do not paste API keys into chat, and rotate any key already shared in a conversation.

Risk: Generated breakdowns and scripts can blur parsed facts with model-inferred creative analysis.

Mitigation: Keep timestamps, speech, and screen text grounded in parsed results, label inferred storyboard details, and manually review claims before publishing or using them commercially.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/xiaohongshu-video-studio)
- [Cue Omni Reader](https://cuecue.cn/hub/omni-reader)
- [Cue API Key Management](https://cuecue.cn/hub/api-key)
- [Cue Remote Omni Reader Endpoint](https://mcp.cuecue.cn/api/omni-reader/mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with tables, structured JSON snippets, and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include inferred storyboard, camera, transition, and emotion notes that should be labeled separately from parsed video facts.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
