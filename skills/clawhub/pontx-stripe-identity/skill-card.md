## Description:

Integrate Stripe Identity safely through Pontx. Use for VerificationSessions, document, selfie, or ID-number checks, webhooks, retries, sensitive results, cancellation, or redaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and implement Stripe Identity verification flows through Pontx while keeping credentials, client secrets, webhook processing, sensitive results, cancellation, and redaction within safe server-side boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stripe credentials, client secrets, webhook payloads, or PII could be exposed through client-side handling, command arguments, logs, analytics, or error tracking.

Mitigation: Keep credentials server-side, return only the client secret to the authenticated user over TLS, verify webhooks against the raw request body, and avoid logging PII or raw events.

Risk: Cancellation and redaction can be irreversible or affect related reports, events, logs, metadata, files, and application-owned copies.

Mitigation: Use dry-run previews, require explicit approval before confirmation, inspect current state, and plan deletion of authorized downstream copies before executing destructive mutations.

Risk: Hardcoded API versions or reconstructed parameters can drift from the live Stripe Identity contract exposed through Pontx.

Mitigation: Load the current Pontx contract and SDK before writing code or running direct scripts, and resolve every mutation through the live contract before previewing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-stripe-identity)
- [Pontx publisher profile](https://clawhub.ai/user/pontjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code-oriented implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
