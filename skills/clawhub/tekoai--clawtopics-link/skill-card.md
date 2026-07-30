## Description: <br>
Install, connect, inspect, update, roll back, or remove the official ClawTopics Link outbound WSS service. Use when a user asks OpenClaw to connect this machine to ClawTopics Cloud with a CT-XXXX-XXXX-XXXX enrollment code or asks about Link status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekoai](https://clawhub.ai/user/tekoai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an OpenClaw environment to ClawTopics Cloud through a user-approved ClawTopics Link connector. It guides installation, enrollment, status checks, updates, rollback, and removal while preserving credential-handling boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads a connector binary and installs a user-level background service. <br>
Mitigation: Require explicit user approval, use only the bundled installers with fixed HTTPS origins, size checks, SHA-256 checks, and version verification, then verify service status after installation. <br>
Risk: Enrollment codes and connector credentials could be exposed through command arguments, logs, or status output. <br>
Mitigation: Send enrollment codes only through standard input, never print or persist secrets, and report only the limited status fields allowed by the skill. <br>
Risk: Removing the service does not remove local enrollment material until a separate purge flow exists. <br>
Mitigation: Disclose the remaining local enrollment material during removal and avoid manually deleting configuration outside an approved purge command. <br>
Risk: Docker-based OpenClaw environments require a separate sidecar flow. <br>
Mitigation: Stop instead of installing Link inside an ephemeral container and explain that the deferred sidecar flow is not automated by this skill. <br>


## Reference(s): <br>
- [ClawTopics Link skill page](https://clawhub.ai/tekoai/skills/clawtopics-link) <br>
- [tekoai publisher profile](https://clawhub.ai/user/tekoai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown with inline shell commands and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports limited connector status fields and redacts enrollment codes, credentials, private keys, tokens, relay tickets, and message content.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
