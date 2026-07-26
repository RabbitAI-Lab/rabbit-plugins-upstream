## Description: <br>
Searches TikTok videos by keyword through Gecho Bridge MCP and returns structured video metadata, creators, engagement metrics, video links, and concise summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, researchers, and developers use this skill to search TikTok for exact keywords, discover videos and creators, collect engagement metadata, and save keyword-level result sets through the official Gecho browser workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TikTok search depends on Gecho Bridge MCP, the Gecho Chrome extension, Chrome, and an active logged-in TikTok web session; missing or blocked prerequisites can cause failures or timeouts. <br>
Mitigation: Confirm the MCP server is configured, the extension is installed and logged in, TikTok web is logged in, and CAPTCHA or login walls are resolved before running a search. <br>
Risk: Search metadata and video links may be saved locally as JSON and could contain sensitive research context. <br>
Mitigation: Use a safe workspace or explicit save directory with appropriate access controls when results could be sensitive. <br>
Risk: Unofficial scraping, parallel scraping jobs, or automatic query rewrites could produce unreliable behavior or unexpected browser-session effects. <br>
Mitigation: Use only the official Gecho `tiktok_search` MCP tool, run one search job per conversational turn, and keep the user's exact keyword unless they provide a new one. <br>


## Reference(s): <br>
- [Tiktok Video Search on ClawHub](https://clawhub.ai/gecho-ai/skills/tiktok-video-search) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [Gecho Website](https://gecho.ai/) <br>
- [OpenClaw TikTok Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes TikTok Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with setup commands, concise search summaries, TikTok video metadata, links, and optional saved JSON result paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the `tiktok_search` MCP tool with a required keyword query and an optional absolute save directory; successful responses should summarize only the top 3 to 5 items.] <br>

## Skill Version(s): <br>
1.1.29 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
