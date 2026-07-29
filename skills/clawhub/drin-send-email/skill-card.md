## Description: <br>
Send a transactional email through Drin reliably. Use when the user or agent needs to send an email (notification, receipt, OTP, alert, password reset, reply) via the Drin email API -- covers picking a verified sending domain, composing the message, sending it, and handling suppressed/rate-limited errors. Works through the @drin00/mcp tools, the drin CLI, the drin SDK, or the raw /v1 REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atom00blue](https://clawhub.ai/user/atom00blue) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to send transactional email through Drin after selecting a verified sending domain, composing content, sending through MCP, CLI, SDK, or REST, and reporting delivery or error outcomes accurately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to send real external email through a Drin account. <br>
Mitigation: Install it only where email sending is intended, and review recipients, sender domain, subject, and message content before sending. <br>
Risk: A broad or mishandled Drin API key could permit unintended email activity. <br>
Mitigation: Use appropriately scoped API keys where possible and provide the required sender context for account-wide keys. <br>
Risk: Queued or scheduled sends may be mistaken for drafts or non-final actions. <br>
Mitigation: Treat queued and scheduled statuses as real external actions and track delivery with Drin email lookup or webhooks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/atom00blue/skills/drin-send-email) <br>
- [Publisher profile](https://clawhub.ai/user/atom00blue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Drin MCP, CLI, SDK, or REST instructions and queued, scheduled, or error status reporting.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
