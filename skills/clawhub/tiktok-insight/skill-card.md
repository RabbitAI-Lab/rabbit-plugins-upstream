## Description: <br>
Run async TikTok product, trend, competitor, and content insight jobs with Gecho Bridge MCP, and check job status. Requires the Gecho Chrome extension, an active TikTok session, and the Gecho Bridge MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to route TikTok product, trend, competitor, and content research requests through the official Gecho Bridge MCP workflow and to check asynchronous insight job status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects AI tools to a logged-in browser session for TikTok research. <br>
Mitigation: Use it only with a TikTok account and browser session you are comfortable exposing to this workflow, then disable the extension or log out when access is no longer needed. <br>
Risk: The required Gecho extension and MCP bridge create a broader browser automation bridge than the skill name alone may imply. <br>
Mitigation: Review the Gecho extension and MCP bridge before installing and use only the official Gecho MCP tools described by the skill. <br>
Risk: Insight jobs can fail or stall when the TikTok tab is logged out, blocked by CAPTCHA, frozen, or unavailable. <br>
Mitigation: Confirm the Gecho extension is online, TikTok web is logged in, and any browser challenges are resolved manually before starting or checking jobs. <br>
Risk: Saved research output may be written to a user-selected directory. <br>
Mitigation: Choose save directories intentionally and avoid paths that expose sensitive local files or shared locations unexpectedly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-insight) <br>
- [Gecho website](https://gecho.ai/) <br>
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and MCP tool result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return asynchronous TikTok insight job IDs, job status, completed insight summaries, setup commands, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.1.30 (source: release evidence and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
