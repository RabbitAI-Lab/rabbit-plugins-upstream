## Description: <br>
Provides Docker-based browser automation with Camoufox and OS-level input for authorized QA, compatibility testing, and defensive security research against systems the user owns or is permitted to test. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and defensive security testers use this skill to control a local browser automation service for authorized testing of anti-bot behavior, compatibility issues, and realistic browser workflows. It is intended for owned systems, in-scope security engagements, sanctioned staging environments, and controlled detection-library research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dual-use browser automation could be applied to unauthorized scraping, access-control evasion, or activity outside the approved test scope. <br>
Mitigation: Use the skill only on systems the operator owns or has written permission to test, and keep test targets, accounts, and workflows explicitly scoped. <br>
Risk: An exposed unauthenticated API or VNC viewer could give another party full control of the browser session. <br>
Mitigation: Bind services to localhost, set AUTH_TOKEN, prefer Authorization headers over query-string tokens, and do not expose VNC beyond local debugging. <br>
Risk: Page capture, screenshots, DOM inspection, cookies, storage, and logs can collect sensitive data from authorized targets. <br>
Mitigation: Capture only what the approved test requires, use isolated test accounts, avoid persistent real session data, and remove mounted profile data after testing. <br>
Risk: Automatic dialog acceptance or URL-triggered loaders can approve destructive actions or modify page state without fresh confirmation. <br>
Mitigation: Disable or tightly scope dialog auto-accept before stateful workflows and mount only loader YAML that has been written or audited by the operator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse) <br>
- [Setup reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON action examples, YAML script examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to issue HTTP or MCP browser actions; service responses can include JSON, page text, HTML, screenshots, recordings, cookies, storage, console logs, and network logs.] <br>

## Skill Version(s): <br>
2.1.4 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
