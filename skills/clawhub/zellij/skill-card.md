## Description: <br>
Remote-control zellij sessions for interactive CLIs by sending keystrokes and scraping pane output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jivvei](https://clawhub.ai/user/jivvei) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage local zellij terminal workspaces for interactive CLIs, including session creation, pane inspection, output polling, and controlled input to terminal processes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over local zellij terminal sessions. <br>
Mitigation: Install only when terminal control is intended, use a dedicated zellij data directory, and verify session and pane IDs before sending input. <br>
Risk: Pane output scraping can expose credentials, private logs, or other sensitive terminal content. <br>
Mitigation: Avoid targeting panes that may display secrets or private logs, and review captured output before sharing it. <br>
Risk: Detached autonomous coding-agent runs can make broad workspace changes when launched with non-interactive flags. <br>
Mitigation: Use autonomous flags only for explicitly requested work in disposable or tightly scoped workspaces. <br>


## Reference(s): <br>
- [Zellij documentation](https://zellij.dev) <br>
- [ClawHub skill page](https://clawhub.ai/jivvei/skills/zellij) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires zellij and jq on macOS or Linux; uses a dedicated zellij data directory by convention.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
