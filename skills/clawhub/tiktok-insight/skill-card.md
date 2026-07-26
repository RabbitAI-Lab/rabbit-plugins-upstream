## Description: <br>
Run async TikTok product, trend, competitor, and content insight jobs through Gecho Bridge MCP, and check existing insight job status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gecho-ai](https://clawhub.ai/user/gecho-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and social commerce researchers use this skill to start TikTok insight jobs for product opportunity analysis, trend discovery, competitor research, and content strategy through Gecho Bridge MCP, then check job status and summarize completed results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on Gecho's MCP bridge and Chrome extension using the user's logged-in browser session to collect TikTok research data. <br>
Mitigation: Confirm trust in the Gecho bridge package and Chrome extension before installation, keep TikTok access within the official Gecho workflow, and review returned insight data before acting on it. <br>
Risk: TikTok insight jobs can fail when MCP tools, the Gecho extension login, the TikTok web login, or the live browser tab are missing or blocked. <br>
Mitigation: Complete the documented setup checklist, keep the extension online and TikTok tab open, and resolve CAPTCHA or login walls manually before retrying. <br>
Risk: Async insight jobs may still be running or may return errors instead of final insight data. <br>
Mitigation: Report the returned jobId, check status later with the official status tool, and avoid inventing conclusions when completed data is unavailable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-insight) <br>
- [Gecho Website](https://gecho.ai/) <br>
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md) <br>
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb) <br>
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ) <br>
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Analysis, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, job IDs, status summaries, and result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a TikTok insight jobId, saved result path, setup instructions, or concise summary of completed insight data.] <br>

## Skill Version(s): <br>
1.1.29 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
