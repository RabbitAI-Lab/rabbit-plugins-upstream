## Description: <br>
Aic Dashboard guides an agent in running a token-protected, local read-only web dashboard that displays recent inbox.jsonl email summaries and session.json browser-session status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and independent operators use this skill to monitor an AI Commander mail collector and browser authentication session from a local dashboard without sending mail, controlling the browser, or modifying the data source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The dashboard reads local email summary and browser-session status files, so anyone with dashboard access can view that local status data. <br>
Mitigation: Install only when that local read-only visibility is acceptable, and keep the default localhost binding unless LAN access is intentionally required. <br>
Risk: Dashboard tokens may appear in URLs and browser storage, and anyone with the token can view the dashboard data. <br>
Mitigation: Use a strong DASHBOARD_TOKEN, avoid sharing token-bearing URLs, and prefer header or Bearer-token access patterns when practical. <br>
Risk: Binding the dashboard to 0.0.0.0 exposes it to other devices on the local network. <br>
Mitigation: Leave DASHBOARD_HOST set to 127.0.0.1 by default; use 0.0.0.0 only for intentional LAN sharing with a strong token. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aic-dashboard) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Clawdis homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides a local read-only dashboard workflow; the dashboard itself displays up to the most recent 50 inbox entries and browser-session status.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
