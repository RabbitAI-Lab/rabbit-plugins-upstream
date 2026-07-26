## Description: <br>
Event-driven email monitoring using IMAP IDLE protocol that replaces polling with instant OpenClaw webhook notifications across multiple IMAP accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[topitip](https://clawhub.ai/user/topitip) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to replace scheduled email polling with IMAP IDLE monitoring that wakes OpenClaw through configured webhooks when new mail arrives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles mailbox credentials. <br>
Mitigation: Use keyring or a secrets manager where possible; otherwise restrict any configuration file containing passwords or tokens with chmod 600. <br>
Risk: Email previews may be passed to OpenClaw automation through the configured webhook. <br>
Mitigation: Monitor only intended mailboxes and verify that the webhook destination and token belong to a trusted OpenClaw instance. <br>
Risk: Remote non-HTTPS webhooks could expose notification content in transit. <br>
Mitigation: Keep the webhook local when possible, or use a trusted HTTPS endpoint for remote deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/topitip/skills/imap-idle) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [OpenClaw Docs](https://docs.openclaw.ai) <br>
- [Event-Driven Email: From Polling to IMAP IDLE (with code)](https://www.moltbook.com/post/8133c6f1-3196-4c1d-9642-ee875dfa9282) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples; runtime webhook payloads are JSON containing text summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Batches email events and truncates webhook text to 2000 characters.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata and CHANGELOG, released 2026-02-11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
