## Description: <br>
Nemesis C2 Bridge lets OpenClaw agents control autonomous WiFi attack agents, dispatch mission chains, query crack jobs, and manage fleet state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mightypi0301-netizen](https://clawhub.ai/user/mightypi0301-netizen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and authorized security operators use this skill to manage OpenClaw-integrated WiFi assessment fleets and dispatch C2 actions during lab or authorized engagements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes high-impact WiFi attack and command-and-control capabilities that can affect third-party networks. <br>
Mitigation: Install only for a lab or authorized security engagement, and require written permission for every target network before use. <br>
Risk: Bridge, heartbeat, fleet, and telemetry endpoints can expose sensitive operational state or precise location data. <br>
Mitigation: Restrict the bridge to trusted networks, use TLS and authentication for heartbeats, and collect precise GPS only when necessary. <br>
Risk: Deauth, evil twin, beacon flooding, downgrade, and kill actions may disrupt service or cause destructive effects. <br>
Mitigation: Require explicit human approval for these actions and review proposed commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mightypi0301-netizen/skills/nemesis-c2-bridge) <br>
- [Publisher profile](https://clawhub.ai/user/mightypi0301-netizen) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, HTTP request examples, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include high-risk WiFi C2 actions that require explicit authorization and human approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
