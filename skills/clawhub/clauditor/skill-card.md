## Description: <br>
Tamper-resistant audit watchdog for Clawdbot agents. Detects and logs suspicious filesystem activity with HMAC-chained evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apollostreetcompany](https://clawhub.ai/user/apollostreetcompany) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use Clauditor to install and operate a Linux audit watchdog for Clawdbot agents, producing tamper-evident logs and digest reports for suspicious filesystem or command activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs persistent Linux services with deliberately stealthy service names and hidden log paths. <br>
Mitigation: Review the installer commands before execution, use guided or dry-run installation where possible, and verify created services and paths after install. <br>
Risk: Privileged install and uninstall steps can alter system services, users, configuration, and audit logs. <br>
Mitigation: Run installation only on intended hosts, require explicit user approval for sudo commands, and preserve or export logs before uninstalling. <br>
Risk: Broad monitoring scope and configurable alert channels can collect sensitive activity or trigger external commands. <br>
Mitigation: Restrict watch paths and target UID to the intended agent account, review alert channels, and keep the HMAC key and configuration permissions tight. <br>


## Reference(s): <br>
- [Clauditor skill page](https://clawhub.ai/apollostreetcompany/skills/clauditor) <br>
- [Clauditor homepage](https://github.com/apollostreetcompany/clauditor) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; CLI status and digest commands can return JSON or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux, systemd, cargo, and privileged user approval for installation steps.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata; artifact Cargo packages report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
