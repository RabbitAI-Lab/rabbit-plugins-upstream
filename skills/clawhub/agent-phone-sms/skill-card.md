## Description:

Agent Phone Number & SMS - Anima helps agents provision real US phone numbers for inbound and outbound SMS and voice calls with transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an AI agent needs a reachable phone number to send texts, receive SMS, place calls, answer calls, and retrieve transcripts through Anima.

### Deployment Geography for Use:

Global; described phone-number provisioning is for geographic US lines.

## Known Risks and Mitigations:

Risk: An external service handles phone numbers, SMS, calls, webhooks, billing, and retained call transcripts.

Mitigation: Confirm retention, consent, privacy, and compliance requirements before installing or using the skill.

Risk: Call transcripts and semantic transcript search can expose privacy-sensitive content.

Mitigation: Avoid secrets or regulated data unless retention, consent, and compliance controls are clear.

Risk: Outbound calling may be refused by consent, plan-cap, or voice-spend gates.

Mitigation: Treat server refusals as an expected control and do not retry around them automatically.

## Reference(s):

- [Anima Documentation](https://docs.useanima.sh)
- [Anima Homepage](https://useanima.sh)
- [Anima API Base](https://api.useanima.sh)
- [ClawHub skill page](https://clawhub.ai/diyanbogdanov/skills/agent-phone-sms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI-oriented guidance for provisioning, listing, releasing, SMS, webhooks, voice calls, and transcript retrieval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
