## Description:

Helps an agent place US phone calls, navigate menus and hold queues, connect users to live calls, and configure ClawCall voice and inbound answering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawcall-dev](https://clawhub.ai/user/clawcall-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their assistants can delegate routine US business calls, follow-ups, bookings, and live handoffs, or set up voice preferences and inbound call answering.

### Deployment Geography for Use:

United States only (US phone numbers)

## Known Risks and Mitigations:

Risk: Calls can incur charges or make commitments on the user's behalf.

Mitigation: Confirm the recipient and decision boundaries before calling; use live handoff for decisions the user must make.

Risk: Call transcripts and recording links may expose personal information, including during live handoff.

Mitigation: Share call records only with the intended user, minimize sensitive details, and do not assume handoff stops recording or transcription.

Risk: The saved API key and sign-in link can grant account access.

Mitigation: Protect the local key store and sign-in link; avoid using shared machines unless access is secured.

Risk: A call may request credentials, payment data, medical information, or other sensitive identity details.

Mitigation: Do not collect or relay restricted details in call instructions; let the user handle sensitive steps through live handoff.

## Reference(s):

- [ClawHub release](https://clawhub.ai/clawcall-dev/skills/clawcall-dev)
- [ClawCall product site](https://clawcall.dev)
- [API contract](artifact/references/api-contract.md)
- [Outbound calling guide](artifact/references/outbound-calls.md)
- [Inbound calling guide](artifact/references/inbound-reserved-numbers.md)
- [Account linking and data guide](artifact/references/account-linking-and-data.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions]

**Output Format:** [Conversational text or Markdown with call results and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include call outcomes, transcripts, and recording links when available.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
