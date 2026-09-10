## Description:

Gives an AI agent a real US phone number for inbound and outbound SMS and voice calls with transcripts in seven languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill when an agent needs its own reachable phone number to send and receive SMS, place or answer voice calls, and retrieve transcripts through Anima.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may trigger paid phone, SMS, or voice usage.

Mitigation: Confirm the intended paid Anima plan before installing, check the active tier with `anima auth whoami`, and have agents request approval instead of retrying refused paid actions.

Risk: Outbound texts or calls may contact real people without proper consent.

Mitigation: Require explicit user consent before outbound communications and respect server-side refusals for TCPA consent, plan caps, or voice spend.

Risk: Inbound SMS webhooks could send real communications to the wrong endpoint.

Mitigation: Verify webhook destinations before enabling `sms.received` delivery.

Risk: Provisioned numbers can remain attached after they are no longer needed.

Mitigation: List and release numbers when work is complete.

Risk: Geographic US lines may be mistaken for mobile numbers or promised for third-party signup checks.

Mitigation: Describe them as geographic US lines and avoid promising that they will pass third-party line-type gates.

## Reference(s):

- [Anima homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima API base](https://api.useanima.sh)
- [ClawHub skill page](https://clawhub.ai/anima/skills/agent-phone-sms)
- [Publisher profile](https://clawhub.ai/user/anima)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers paid phone number provisioning, SMS, webhooks, voice calls, and transcript retrieval.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
