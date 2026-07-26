## Description: <br>
Set up and call the gtm-tools API from an agent to get an API key, connect browser-backed LinkedIn and Reddit sessions, and use GTM data tools through Bash, curl, MCP, or the gtm-tools CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnaudjnn](https://clawhub.ai/user/arnaudjnn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to onboard agents to gtm-tools, manage API keys and token metering, connect account sessions, and call LinkedIn, Reddit, email, buying-signal, and geocoding tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent create or claim API credentials and connect account sessions. <br>
Mitigation: Require explicit user approval before account creation, identity claims, browser-extension installation, or use of logged-in LinkedIn and Reddit sessions. <br>
Risk: The skill includes billing and token-management actions such as buying tokens and enabling auto-reload. <br>
Mitigation: Require confirmation before purchases, auto-reload changes, or actions that may consume paid tokens; check token balance and live costs before high-volume runs. <br>
Risk: Session-backed tools can read private account surfaces or perform social actions such as messages, posts, votes, and replies. <br>
Mitigation: Scope which connected account may be used and require review before reading inboxes, conversations, saved items, or taking write actions. <br>
Risk: Retries and fan-out calls can increase cost because some failed or not-found results may still be metered. <br>
Mitigation: Use the free balance and connected-account checks first, filter targets before expensive calls, and honor retry-after guidance instead of tight retry loops. <br>


## Reference(s): <br>
- [GTM Tools full tool catalog](references/tools.md) <br>
- [Agent authentication protocol](https://api.gtm-tools.sh/auth.md) <br>
- [GTM Tools agent docs index](https://gtm-tools.sh/llms.txt) <br>
- [GTM Tools API reference](https://gtm-tools.sh/api-reference) <br>
- [ClawHub skill page](https://clawhub.ai/arnaudjnn/skills/gtm-tools) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Bash, curl, JSON request bodies, tables, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to make authenticated API, MCP, CLI, browser-extension, billing, and session-backed social-media calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
