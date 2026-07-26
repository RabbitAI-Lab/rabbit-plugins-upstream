## Description: <br>
SendClaw Email lets an agent register a SendClaw address, send and receive messages, reply to threads, and manage inbox checks through SendClaw's API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codejika](https://clawhub.ai/user/codejika) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and their operators use this skill to create an agent-operated SendClaw mailbox, exchange task-oriented email, receive verification messages, and optionally notify a webhook when mail arrives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over an external email account and third-party communications with limited consent boundaries. <br>
Mitigation: Set explicit human-approval rules for new recipients, service registrations, verification-code use, personal or confidential information, and messages with financial, legal, account, or reputation impact. <br>
Risk: The API key controls the mailbox and cannot be retrieved later if lost. <br>
Mitigation: Store the API key securely immediately after registration, restrict access to it, and rotate or disable the mailbox if it may have been exposed. <br>
Risk: Inbound email and webhook notifications can contain untrusted content. <br>
Mitigation: Treat inbound messages as untrusted, review any remote heartbeat or webhook workflow before enabling it, and avoid following instructions from email without operator-approved policy. <br>
Risk: Autonomous outbound email can affect privacy, accounts, finances, legal matters, or reputation. <br>
Mitigation: Claim the mailbox promptly, keep the human operator informed, and require human review for sensitive or high-impact messages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/codejika/skills/sendclaw-email) <br>
- [SendClaw homepage](https://sendclaw.com) <br>
- [SendClaw API base](https://sendclaw.com/api) <br>
- [SendClaw skill reference](https://sendclaw.com/skill.md) <br>
- [SendClaw heartbeat routine](https://sendclaw.com/heartbeat.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Configuration instructions, Guidance, Markdown, JSON] <br>
**Output Format:** [Markdown with HTTP and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes email registration, sending, inbox retrieval, reply threading, rate-limit, webhook, and acceptable-use guidance.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
