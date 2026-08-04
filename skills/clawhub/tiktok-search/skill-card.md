## Description: <br>
Search TikTok videos, collect creator videos, and run product, trend, competitor, and content insights through Gecho Bridge MCP, requiring the Gecho Chrome extension, an active TikTok session, and the Gecho Bridge MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search TikTok, collect structured creator and video metadata, and start product, trend, competitor, or content insight jobs through Gecho Bridge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TikTok workflows will not run unless Gecho Bridge MCP, the Gecho Chrome extension, a logged-in Gecho account, and a logged-in TikTok web session are configured. <br>
Mitigation: Complete the documented setup steps and verify that the official Gecho MCP tools are available before attempting a search or insight job. <br>
Risk: The workflow uses a live browser session and Chrome extension to collect TikTok metadata. <br>
Mitigation: Review the external MCP package and extension permissions, and avoid using accounts or browser sessions that contain sensitive private activity unless the integration is trusted. <br>
Risk: Result saving can fail or write to an unintended location when the save directory is unreliable. <br>
Mitigation: Use a known absolute directory with appropriate write permissions, or omit the save directory and let Gecho use its default data location. <br>
Risk: Login walls, CAPTCHA, frozen pages, network issues, or TikTok session problems can block collection. <br>
Mitigation: Resolve browser-side blocks manually, stop on tool errors or timeouts, and report the exact failure instead of retrying automatically. <br>
Risk: TikTok insight jobs are asynchronous and may not complete in the same turn. <br>
Mitigation: Return the job ID, tell the user the job can take several minutes, and check status later with the official status tool. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-search) <br>
- [Gecho website](https://gecho.ai/) <br>
- [Gecho Bridge repository](https://github.com/gecho-ai/gecho-bridge) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and summarized JSON-like MCP/tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include saved local file paths and summarized TikTok metadata; full raw result sets are saved to files rather than pasted.] <br>

## Skill Version(s): <br>
1.1.30 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
