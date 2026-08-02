## Description: <br>
Collects public videos from a TikTok creator with Gecho Bridge MCP, returning video metadata, captions, engagement metrics, publish times, and links while requiring the Gecho Chrome extension, an active TikTok session, and the Gecho Bridge MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, and social-media analysts use this skill to collect and summarize recent videos from a single TikTok creator profile through the Gecho Bridge MCP workflow. It is useful when the user has a working Gecho Chrome extension, an active TikTok browser session, and wants structured creator-video data rather than a generic web search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on Gecho Bridge MCP, the Gecho Chrome extension, and a live TikTok browser session, so it can fail when setup is incomplete or the page is blocked by login, CAPTCHA, verification, region, or cookie prompts. <br>
Mitigation: Confirm the MCP server, extension login, and TikTok tab are ready before collection; resolve browser prompts manually and report exact setup or tool errors without retrying automatically. <br>
Risk: The MCP server and Chrome extension interact with an active browser session and may save collected results locally. <br>
Mitigation: Install only when comfortable with this browser-session workflow, review setup commands before running them, and save exports inside the workspace or a dedicated export folder. <br>
Risk: Returned creator-video data may be empty, incomplete, or unavailable for a given profile. <br>
Mitigation: Summarize only data returned by the official Gecho MCP tool, avoid inventing results, and stop with a clear message when no collectable videos are returned. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer) <br>
- [Gecho Website](https://gecho.ai/) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance] <br>
**Output Format:** [Markdown guidance with setup commands and summarized JSON result metadata; saved results are JSON when the MCP tool writes an output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful runs should summarize only the top 3 to 5 videos and include the saved file path when available.] <br>

## Skill Version(s): <br>
1.1.30 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
