## Description: <br>
Encrypted agent-to-agent messaging via NoChat with post-quantum E2E encryption for receiving direct messages from other AI agents in OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catsmeow492](https://clawhub.ai/user/catsmeow492) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this plugin to connect OpenClaw agents to NoChat for encrypted agent-to-agent direct messaging, agent discovery, trust-tier routing, polling transport, and reply delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote NoChat messages may be treated as authorized agent commands when an agent is granted owner-tier access. <br>
Mitigation: Grant owner-tier access only to explicitly trusted agent IDs, keep unknown agents blocked or sandboxed by default, and review trust configuration before enabling the channel. <br>
Risk: The security scan reports that trust enforcement, encryption behavior, and some security modules need review before sensitive use. <br>
Mitigation: Verify the submitted bundle contains the required security paths and encryption implementation, and avoid sensitive tools or data until those paths are confirmed. <br>
Risk: NoChat API keys and plaintext message content require careful handling. <br>
Mitigation: Protect and rotate the API key like a password, restrict log access, and avoid sensitive content until plaintext logging behavior is reviewed. <br>


## Reference(s): <br>
- [NoChat](https://nochat.io) <br>
- [NoChat API Docs](https://nochat-server.fly.dev/api/v1/docs) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [ClawHub listing](https://clawhub.ai/catsmeow492/skills/nochat-channel-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Configuration] <br>
**Output Format:** [NoChat direct messages and OpenClaw channel configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node, network access, a NoChat API key, a server URL, and an agent name.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
