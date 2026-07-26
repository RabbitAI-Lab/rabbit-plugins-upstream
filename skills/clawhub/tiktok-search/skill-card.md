## Description: <br>
Search TikTok videos, collect creator videos, and run product, trend, competitor, and content insights through Gecho Bridge MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search TikTok, collect creator and video metadata, and run product, trend, competitor, or content insight workflows through Gecho Bridge MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on a third-party MCP server and Chrome extension connected to a logged-in TikTok browser session. <br>
Mitigation: Use it only when comfortable with Gecho accessing TikTok data visible in that browser session, and keep the extension and TikTok session limited to the intended research account. <br>
Risk: The skill saves raw TikTok research results to local JSON files. <br>
Mitigation: Choose a trusted save directory and review saved files before sharing or retaining them. <br>
Risk: TikTok search or insight features may fail if the MCP server, Chrome extension, Gecho login, or TikTok login is missing. <br>
Mitigation: Complete the documented Gecho Bridge setup, keep the extension online, and keep a logged-in TikTok tab open before running searches. <br>


## Reference(s): <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [Gecho Website](https://gecho.ai/) <br>
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>
- [Gecho Support Discord](https://discord.gg/RFDVZMR6Tn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API calls, Files] <br>
**Output Format:** [Markdown with setup commands, JSON result summaries, job IDs, and local file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful searches summarize the top 3 to 5 items; insight jobs return a jobId and require a later status check.] <br>

## Skill Version(s): <br>
1.1.29 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
