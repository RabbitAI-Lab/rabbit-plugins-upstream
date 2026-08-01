## Description: <br>
Search TikTok videos by keyword with Gecho Bridge MCP and return video metadata, creators, engagement metrics, and links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and social-media researchers use this skill to route TikTok keyword search requests through Gecho Bridge MCP, summarize the top video results, and provide creator, engagement, metadata, link, and saved-result details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses Gecho Bridge and its Chrome extension with a logged-in TikTok browser session. <br>
Mitigation: Install only when that browser-session workflow is acceptable, keep required sessions under user control, and stop on login walls, CAPTCHA, timeouts, or tool errors. <br>
Risk: Saved search-result JSON files can contain sensitive research records on shared machines. <br>
Mitigation: Choose a trusted save directory, avoid pasting full raw JSON into chat, and clean saved files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-video-search) <br>
- [Gecho Website](https://gecho.ai/) <br>
- [Gecho Bridge GitHub and README](https://github.com/gecho-ai/gecho-bridge) <br>
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown summaries with TikTok result links, setup commands when needed, and saved JSON file paths when results are written.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the Gecho MCP tiktok_search tool with a required query and optional save_dir; successful responses summarize 3 to 5 results rather than pasting full raw JSON.] <br>

## Skill Version(s): <br>
1.1.30 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
