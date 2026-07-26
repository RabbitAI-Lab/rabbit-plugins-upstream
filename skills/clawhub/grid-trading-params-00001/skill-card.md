## Description: <br>
Safely install and run the bundled 00001 Grid Trading Bot in demo or sandbox mode, preview grid parameters, and generate paste-ready key=value or JSON configuration. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[frederica123](https://clawhub.ai/user/frederica123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to install, configure, preview, start, stop, and troubleshoot a local grid-trading demo lab without exposing live trading credentials in chat. It is intended for exchange demo or sandbox environments only, not production trading or live funds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may accidentally enter live exchange credentials or attempt to use live funds. <br>
Mitigation: Use demo or sandbox API credentials only, keep paper/demo mode enabled, and rotate any credentials if live keys are entered by mistake. <br>
Risk: Exposing the local trading service could reveal controls or sensitive inputs outside the user's machine. <br>
Mitigation: Keep the service bound to 127.0.0.1 and do not expose it through tunnels, port forwarding, public firewall rules, or reverse proxies. <br>
Risk: Credentials are sensitive even when intended for a sandbox exchange account. <br>
Mitigation: Enter credentials only in the local page; do not paste them into chat, commands, screenshots, issues, logs, or saved config files. <br>
Risk: Grid trading output can be misunderstood as investment advice or a profit guarantee. <br>
Mitigation: Treat generated parameters as demo-lab configuration only and make clear that sandbox results do not predict live performance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/frederica123/skills/grid-trading-params-00001) <br>
- [Publisher profile](https://clawhub.ai/user/frederica123) <br>
- [Artifact README](bot/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and key=value or JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates local setup steps, parameter previews, sandbox-only configuration, and troubleshooting guidance; it should not collect or echo credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and bot/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
