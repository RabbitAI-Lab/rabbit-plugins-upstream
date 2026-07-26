## Description: <br>
A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gwqwghksvq-sketch](https://clawhub.ai/user/gwqwghksvq-sketch) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to automate browser workflows such as navigation, page inspection, form filling, UI testing, screenshots, PDF export, and session reuse through the agent-browser CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over browser sessions, including authenticated sessions. <br>
Mitigation: Install it only when full browser automation is needed, and avoid using it on sensitive authenticated accounts unless that access is explicitly intended. <br>
Risk: Saved browser state, screenshots, recordings, traces, headers, credentials, and auth files can expose sensitive data. <br>
Mitigation: Treat those artifacts like secrets, keep them out of shared folders and source control, and delete them when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gwqwghksvq-sketch/skills/tekin) <br>
- [agent-browser CLI repository](https://github.com/vercel-labs/agent-browser) <br>
- [Agent Browser skill issue repository](https://github.com/TheSethRose/Agent-Browser-CLI) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, JSON, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI commands may return text or JSON and may write screenshots, PDFs, videos, traces, and browser state files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm; browser automation can create local session, media, trace, and state artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
