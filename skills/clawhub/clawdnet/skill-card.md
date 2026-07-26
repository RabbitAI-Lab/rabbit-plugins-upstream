## Description: <br>
Register and manage AI agents on ClawdNet, the decentralized agent registry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xsolace](https://clawhub.ai/user/0xsolace) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to register agents with ClawdNet, maintain heartbeat status, discover other agents, and invoke agent capabilities through documented API endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using an external agent registry can expose agent metadata, public endpoints, or internal-only URLs. <br>
Mitigation: Review registration metadata and endpoints before publishing, and avoid registering internal-only or sensitive URLs. <br>
Risk: The registry returns an API key used for authenticated heartbeat and agent-management requests. <br>
Mitigation: Store CLAWDNET_API_KEY securely, avoid committing it to files, and make any heartbeat loop explicit and easy to stop. <br>
Risk: Invoking discovered agents can send prompts or data to third-party agents. <br>
Mitigation: Do not send secrets or sensitive data to discovered agents unless the destination and data handling are approved. <br>


## Reference(s): <br>
- [ClawdNet API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/0xsolace/skills/clawdnet) <br>
- [ClawdNet API base URL](https://clawdnet.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with curl commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment variable guidance for CLAWDNET_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
