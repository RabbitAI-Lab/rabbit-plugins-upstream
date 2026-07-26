## Description: <br>
Protect AI agents from email-based attacks including prompt injection, sender spoofing, malicious attachments, and social engineering. Use when processing emails, reading email content, executing email-based commands, or any interaction with email data. Provides sender verification, content sanitization, and threat detection for Gmail, AgentMail, Proton Mail, and any IMAP/SMTP email system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivaavimusic](https://clawhub.ai/user/ivaavimusic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to add defensive checks before an agent reads, parses, or acts on email. It helps verify senders, sanitize email content, detect prompt injection and spoofing indicators, and enforce attachment handling policies across Gmail, AgentMail, Proton Mail, and generic IMAP/SMTP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Owner and admin email addresses may be granted automatic command authority if configured too broadly. <br>
Mitigation: Require explicit confirmation for every command execution, keep owner/admin/trusted lists narrow, and restrict the set of email commands the agent may perform. <br>
Risk: Full-message logging can preserve sensitive or malicious email content. <br>
Mitigation: Use flagged-only or blocked-only logging unless a protected forensic workflow is in place, and redact sensitive fields from retained logs. <br>
Risk: Attachments saved from email remain untrusted even when the filename extension is allowed. <br>
Mitigation: Store attachments in a quarantined location, scan them before use, block executable/script formats, and avoid OCR on images from untrusted senders. <br>
Risk: Sender identity checks can be bypassed by spoofing, look-alike domains, or weak authentication headers. <br>
Mitigation: Validate SPF, DKIM, and DMARC results when available; compare From, Reply-To, Return-Path, and domain similarity; and require confirmation on authentication failures. <br>


## Reference(s): <br>
- [Security Policies](references/security-policies.md) <br>
- [Threat Patterns](references/threat-patterns.md) <br>
- [Owner Configuration](references/owner-config.md) <br>
- [Gmail Provider Guide](references/provider-gmail.md) <br>
- [AgentMail Provider Guide](references/provider-agentmail.md) <br>
- [Generic Email Provider Guide](references/provider-generic.md) <br>
- [Security Configuration Template](assets/security-config-template.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON, Text] <br>
**Output Format:** [Markdown guidance with shell command examples, Python helper scripts, JSON configuration, and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes sender-verification, content-sanitization, email-parsing, attachment-policy, and provider-specific security guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
