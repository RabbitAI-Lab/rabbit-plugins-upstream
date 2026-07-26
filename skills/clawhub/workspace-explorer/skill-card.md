## Description: <br>
Workspace Explorer helps an agent provide temporary browser-based VS Code access to a selected workspace for trusted remote inspection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrbeandev](https://clawhub.ai/user/mrbeandev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill when a trusted owner needs temporary live IDE access to inspect working files, browse a codebase, or use editor features during a support session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A public tunnel can expose the selected workspace to anyone who obtains the URL and password. <br>
Mitigation: Serve the smallest sanitized directory possible, remove secrets and credentials first, share access only with the intended trusted recipient, and stop the tunnel as soon as the session is finished. <br>
Risk: The skill relies on external code and binary downloads. <br>
Mitigation: Review the external repository and start script before use, and install only when live browser-based IDE access is intentionally needed. <br>
Risk: A workspace session may remain active longer than intended. <br>
Mitigation: Use the status check and heartbeat guidance to monitor active sessions, alert the owner for long-running tunnels, and terminate unused sessions. <br>


## Reference(s): <br>
- [Workspace Explorer ClawHub listing](https://clawhub.ai/mrbeandev/skills/workspace-explorer) <br>
- [Workspace Explorer repository](https://github.com/mrbeandev/workspace-explorer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tunnel setup commands, status-check commands, and instructions for handling the public URL and password.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
