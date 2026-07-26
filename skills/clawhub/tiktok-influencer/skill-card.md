## Description: <br>
Collect videos published by a TikTok influencer or creator through Gecho Bridge MCP and return structured video metadata, captions, engagement metrics, publish times, and video links when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect and summarize video metadata from a specific TikTok creator profile for creator research, influencer due diligence, and content analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow connects Gecho's Chrome extension and MCP bridge to an active TikTok web session. <br>
Mitigation: Install only if that connection is acceptable, review the Gecho extension and bridge package before use, and keep login, CAPTCHA, and verification steps manual. <br>
Risk: Saved result files may be written to a local directory selected during the workflow. <br>
Mitigation: Use a dedicated local save directory that does not expose sensitive files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer) <br>
- [Gecho website](https://gecho.ai/) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>
- [Gecho YouTube channel](https://www.youtube.com/@Gecho-AI) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and summarized JSON metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful runs summarize the top 3 to 5 videos and include a saved local JSON file path when available.] <br>

## Skill Version(s): <br>
1.1.29 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
