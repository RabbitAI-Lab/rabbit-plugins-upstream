## Description: <br>
Drive a machine with a real hardware keyboard and mouse via Rebind to click, type, browse, fill forms, and operate desktop GUI applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[usinput](https://clawhub.ai/user/usinput) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to let an OpenClaw agent operate Windows or macOS desktop applications through Rebind-controlled keyboard and mouse input. It is suited for GUI tasks such as browsing, form entry, window control, and visual checkpoint verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad control of the connected desktop and local scripting interfaces. <br>
Mitigation: Use it only on a machine or profile where that level of control is acceptable, and prefer an isolated environment for higher-risk tasks. <br>
Risk: An exposed or weakly protected Rebind relay could allow unwanted desktop control. <br>
Mitigation: Protect the relay with an auth token and keep access limited to the intended local endpoint. <br>
Risk: The MCP package may change between installs if it is fetched without a fixed version. <br>
Mitigation: Consider pinning the MCP package version before deployment. <br>
Risk: GUI automation can perform irreversible or outbound actions such as submissions, deletions, payments, or public posts. <br>
Mitigation: Require explicit user confirmation before irreversible or outbound actions and verify at checkpoints before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/usinput/skills/rebind-computer-use) <br>
- [Rebind homepage](https://rebind.gg) <br>
- [Rebind download](https://rebind.gg/download) <br>
- [@rebind.gg/mcp-server package](https://www.npmjs.com/package/@rebind.gg/mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell, JSON, and Luau examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides an agent through desktop-control workflows and checkpoint verification.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
