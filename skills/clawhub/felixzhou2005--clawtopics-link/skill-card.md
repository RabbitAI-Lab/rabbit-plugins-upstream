## Description: <br>
Installs, connects, inspects, updates, rolls back, or removes the official ClawTopics Link outbound WSS service for OpenClaw enrollment and status workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[felixzhou2005](https://clawhub.ai/user/felixzhou2005) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to enroll an OpenClaw host with ClawTopics Cloud, manage the user-level ClawTopics Link service, and check status while protecting enrollment codes and connector credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and enrolling ClawTopics Link connects the local device to ClawTopics Cloud. <br>
Mitigation: Require explicit user approval before downloading, installing, enrolling, updating, rolling back, or removing the user-level service. <br>
Risk: Enrollment codes, connector credentials, private keys, device tokens, relay tickets, or message content could be exposed during setup or troubleshooting. <br>
Mitigation: Send enrollment codes only through standard input when supported, never print or persist secrets, and redact credentials, tokens, keys, and sensitive message content from reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/felixzhou2005/skills/clawtopics-link) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Status reporting is limited to non-sensitive connector and installation details with credentials, tokens, keys, and enrollment codes redacted.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
