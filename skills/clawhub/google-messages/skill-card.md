## Description: <br>
Send and receive SMS/RCS via the Google Messages web interface, including optional forwarding of incoming message notifications to configured OpenClaw channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kesslerio](https://clawhub.ai/user/kesslerio) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
External users and developers use this skill to automate SMS/RCS workflows through a paired Google Messages web session, including sending texts, checking conversations, and optionally forwarding incoming message previews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incoming SMS previews may be forwarded to another channel. <br>
Mitigation: Keep notification forwarding disabled unless the destination is trusted, and avoid forwarding authentication codes or sensitive conversations. <br>
Risk: The notification webhook can execute shell commands built from message content. <br>
Mitigation: Do not enable the webhook or persistent service until the forwarding path has been fixed or contained, and run it with the least privileges practical. <br>
Risk: A paired browser profile can access Google Messages for the linked phone. <br>
Mitigation: Use a dedicated browser profile, pair only on a trusted machine, and treat QR pairing and session cookies as sensitive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kesslerio/skills/google-messages) <br>
- [Publisher Profile](https://clawhub.ai/user/kesslerio) <br>
- [Google Messages Web](https://messages.google.com/web) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Observer Injection](references/observer-injection.md) <br>
- [JavaScript Snippets](references/snippets.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with browser automation commands, shell commands, and JavaScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a paired Google Messages web session, a persistent browser profile, Node.js, and notification environment variables when forwarding is enabled.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
