## Description:

ClawCall lets an AI agent place real US phone calls, navigate phone trees and hold time, optionally bridge the user into a live call, and return call outcomes, transcripts, and recording links when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shreyjindal81](https://clawhub.ai/user/shreyjindal81)

### License/Terms of Use:

MIT-0

## Use Case:

External end users and agents use this skill to delegate routine US phone work such as booking, confirming, rescheduling, canceling, checking order or appointment status, comparing business options, reaching a live person, or configuring ClawCall voice, personality, and inbound reserved-number answering.

### Deployment Geography for Use:

United States only; the artifact states that the skill validates +1 E.164 numbers and does not support international calls.

## Known Risks and Mitigations:

Risk: The skill can place real phone calls that may create commitments, costs, or unwanted contact with third parties.

Mitigation: Review call instructions before execution, include explicit decision boundaries, and use live handoff for sensitive, negotiable, identity-heavy, payment, or OTP-related calls.

Risk: The skill can persist and reuse a ClawCall API key and the user's phone number.

Mitigation: Prefer a secure secret store, rotate exposed keys, and only save or reuse phone numbers when the user is comfortable with ongoing use.

Risk: Account-link URLs can contain tokens that grant access to the user's ClawCall session context.

Mitigation: Preserve returned URLs exactly, do not share account-link URLs broadly, and replace or rotate keys if a token-bearing URL is exposed.

Risk: The skill can access call transcripts, recording links, and inbound call history that may contain sensitive personal information.

Mitigation: Treat transcripts and recording links as sensitive, summarize only what is needed, and enable inbound answering or polling only when the user accepts the privacy implications.

Risk: The skill can alter global ClawCall voice, personality, greeting, and inbound answering preferences.

Mitigation: Read current preferences before changes, preserve existing global settings when editing only inbound behavior, and confirm persistent profile changes with the user.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [API contract](artifact/references/api-contract.md)
- [Outbound calls](artifact/references/outbound-calls.md)
- [Inbound reserved numbers](artifact/references/inbound-reserved-numbers.md)
- [Account linking and data](artifact/references/account-linking-and-data.md)
- [Errors and limits](artifact/references/errors-and-limits.md)
- [Profile and personality](artifact/references/profile-and-personality.md)
- [Examples](artifact/references/examples.md)
- [Pressure scenarios](artifact/evals/pressure-scenarios.md)
- [ClawCall product site](https://clawcall.dev)
- [Agent Skills open specification](https://agentskills.io/specification)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and HTTP request examples; API interactions return JSON call status, transcript, outcome, and recording metadata when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may persist a ClawCall API key and user phone number, place real US phone calls, poll call status, configure voice and inbound preferences, and surface transcript or recording links.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
