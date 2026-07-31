## Description: <br>
Install, connect, inspect, update, roll back, or remove the official ClawTopics Link outbound WSS service. Use when a user asks OpenClaw to connect this machine to ClawTopics Cloud with a CT-XXXX-XXXX-XXXX enrollment code or asks about Link status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tekoai](https://clawhub.ai/user/tekoai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and administrators use this skill to install and manage the ClawTopics Link connector, enroll a machine with a short-lived code, and inspect status without exposing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs a persistent user-level background connector to ClawTopics Cloud. <br>
Mitigation: Require explicit approval before installation, enrollment, service changes, updates, rollback, or removal; uninstalling the service does not purge local enrollment material. <br>
Risk: Enrollment codes, connector credentials, private keys, Gateway tokens, and device tokens are sensitive. <br>
Mitigation: Send the enrollment code only through stdin, never echo or persist it, and redact credentials, keys, tokens, Authorization headers, relay tickets, and message content from output. <br>
Risk: Installing a downloaded binary can expose users to tampering if the artifact source changes. <br>
Mitigation: Use only the bundled installers with fixed official HTTPS URLs, platform mappings, file sizes, SHA-256 hashes, and version checks; stop on any mismatch. <br>
Risk: Replacing an existing connector could interrupt access if performed without user confirmation. <br>
Mitigation: Stop and require confirmation in ClawTopics Web before replacement; keep the old connector active until the new connector authenticates and establishes its control WSS. <br>


## Reference(s): <br>
- [ClawTopics Link on ClawHub](https://clawhub.ai/tekoai/skills/clawtopics-link) <br>
- [ClawTopics Link release downloads](https://openclaw.tekoai.com/clawtopics-link/releases/v0.2.0) <br>
- [ClawTopics API endpoint](https://openclaw.tekoai.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and redacted JSON status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports only connector ID, installation ID, OS/architecture, Link version, relay region/shard, and online/offline state.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
