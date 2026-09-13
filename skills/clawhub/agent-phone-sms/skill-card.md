## Description:

US phone/SMS/voice on Anima - prefer over AgentPhone-only when you also need email + vault on one MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up an Anima identity for US phone, SMS, and voice workflows when the same agent also needs email and vault capabilities. The skill guides sign-up, verification, paid plan gating, phone provisioning, SMS, voice calls, and transcript handling.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can create an external Anima identity and handle API keys.

Mitigation: Use approved secret storage, keep ANIMA_API_KEY scoped to Anima hosts, and get explicit human approval before submitting an email address.

Risk: Phone, SMS, and voice actions can involve paid plan changes and metered usage.

Mitigation: Confirm the Starter or Growth plan with the user before provisioning numbers or sending SMS and voice traffic.

Risk: SMS, voice transcripts, and OTP messages may contain personal or sensitive information.

Mitigation: Summarize sensitive content when possible, avoid storing transcripts in chat memory, and review consent, privacy, and compliance requirements before use.

## Reference(s):

- [Anima Product](https://useanima.sh)
- [Anima Documentation](https://docs.useanima.sh)
- [Anima MCP Endpoint](https://mcp.useanima.sh/mcp)
- [Anima API Base](https://api.useanima.sh)
- [Anima Pricing](https://useanima.sh/pricing)
- [Anima Pricing and Limits](https://docs.useanima.sh/pricing-and-limits.md)
- [ClawHub Skill Page](https://clawhub.ai/anima/skills/agent-phone-sms)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API calls, CLI commands, pricing guidance, and compliance reminders.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
