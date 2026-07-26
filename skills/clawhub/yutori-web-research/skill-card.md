## Description: <br>
Use Yutori's Research API and Browsing API (cloud browser) to research topics, collect sources, and extract structured facts from the web. Use when the user asks to "research X", "monitor/find papers", or "navigate to a site and extract info" and you have access to YUTORI dev/prod endpoints via YUTORI_API_BASE and an API key in env (YUTORI_API_KEY or ~/.openclaw/openclaw.json env.YUTORI_API_KEY). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanpin](https://clawhub.ai/user/juanpin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to delegate web research and cloud-browser navigation tasks to Yutori, then return concise briefs, source-backed reading lists, or extracted site facts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts, URLs, and browsing tasks are sent to Yutori's cloud service. <br>
Mitigation: Avoid sending confidential/internal URLs, secrets, or sensitive prompts unless approved for Yutori processing. <br>
Risk: The skill depends on a Yutori API key and configurable API endpoint. <br>
Mitigation: Use a limited Yutori API key and verify YUTORI_API_BASE points to the intended dev or production endpoint. <br>
Risk: Browsing tasks may include form submissions or other state-changing website actions. <br>
Mitigation: Confirm before form submissions or other state-changing browsing tasks. <br>


## Reference(s): <br>
- [Yutori website](https://yutori.com) <br>
- [Yutori production API endpoint](https://api.yutori.com) <br>
- [Yutori development API endpoint](https://api.dev.yutori.com) <br>
- [ClawHub skill page](https://clawhub.ai/juanpin/skills/yutori-web-research) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text with bullets, source URLs, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Research and browsing tasks require a Yutori API key and send prompts, URLs, and browsing instructions to Yutori's cloud service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
