## Description: <br>
Drive THIS computer with a real hardware keyboard and mouse via Rebind — click, type, browse, fill forms, operate any desktop GUI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rebind](https://clawhub.ai/user/rebind) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent control a Windows or macOS desktop through Rebind for browser and desktop GUI workflows. It is suited to tasks such as browsing, filling forms, operating applications, and verifying visual checkpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables practical control of the user's desktop, and its scripting path can reach local files, processes, network access, clipboard, environment variables, and registry data. <br>
Mitigation: Install only when the Rebind app and MCP package are trusted, keep the relay off when not actively using it, and treat run_lua as elevated local access. <br>
Risk: GUI control can perform irreversible or outbound actions such as submitting forms, sending messages, making payments, deleting data, or posting publicly. <br>
Mitigation: Require explicit user confirmation before irreversible or outbound actions, summarizing the intended recipient, amount, content, or data change first. <br>
Risk: Desktop automation may expose credentials, payment details, or two-factor codes visible in the active session. <br>
Mitigation: Do not enter or handle credentials, payment details, or 2FA codes unless the user supplied them in the current conversation for that exact purpose. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rebind/skills/computer-use) <br>
- [Rebind download](https://rebind.gg/download) <br>
- [@rebind.gg/mcp-server package](https://www.npmjs.com/package/@rebind.gg/mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands and Luau code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Rebind relay, REBIND_URL, bun, and the Rebind MCP server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
