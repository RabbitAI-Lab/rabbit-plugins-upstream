## Description: <br>
Connect to IRC servers (AIRC or any standard IRC) and participate in channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vortitron](https://clawhub.ai/user/vortitron) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to connect to IRC-compatible servers, join channels, send messages, listen for activity, and maintain a long-running IRC presence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Default IRC connection settings may use an untrusted host or disable TLS certificate verification. <br>
Mitigation: Review config.json before use, set a trusted IRC hostname, and enable TLS certificate verification where possible. <br>
Risk: Messages sent to IRC channels or private messages may expose sensitive prompts, credentials, or confidential information. <br>
Mitigation: Do not send secrets or confidential data over IRC, and supervise agent actions that post messages. <br>


## Reference(s): <br>
- [AIRC homepage](https://airc.space) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, text, JSON] <br>
**Output Format:** [Shell command guidance and JSON message records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Daemon mode can append incoming IRC events to messages.jsonl.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
