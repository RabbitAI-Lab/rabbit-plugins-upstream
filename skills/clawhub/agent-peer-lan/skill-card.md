## Description: <br>
Connect two OpenClaw agents on the same LAN as peer collaborators with direct sessions_send communication on a trusted local network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hypnotronic3](https://clawhub.ai/user/hypnotronic3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure two OpenClaw agents on trusted LAN machines so they can send messages, delegate work, and share context without a VPN or third-party relay. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to expose an OpenClaw gateway on a LAN, which can expand access to agent sessions if the network is not trusted or scoped. <br>
Mitigation: Bind the gateway to a specific trusted LAN IP when possible and restrict firewall rules to the trusted subnet. <br>
Risk: Gateway tokens may be mishandled while setting up peer communication. <br>
Mitigation: Require an auth token when the gateway supports it, avoid storing tokens in peer config files, and pass tokens at runtime or through environment variables. <br>
Risk: Applying broad gateway, firewall, or routing changes can unintentionally expose the service beyond the intended LAN. <br>
Mitigation: Review gateway binding, firewall rules, and subnet routing before applying changes, and avoid public or guest networks. <br>


## Reference(s): <br>
- [Network Setup - LAN Peer Agent](references/network-setup.md) <br>
- [Troubleshooting - LAN Peer Agent](references/troubleshooting.md) <br>
- [Agent Peer Lan on ClawHub](https://clawhub.ai/hypnotronic3/skills/agent-peer-lan) <br>
- [hypnotronic3 publisher profile](https://clawhub.ai/user/hypnotronic3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and an optional generated peer-config.md file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include LAN gateway URLs, firewall rules, connectivity checks, and runtime token-handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
