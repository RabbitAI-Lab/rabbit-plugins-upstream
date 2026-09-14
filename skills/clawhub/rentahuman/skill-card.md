## Description:

Hire humans for physical-world tasks via RentAHuman.ai by searching profiles, posting bounties, starting conversations, and coordinating real-world work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexanderliteplo](https://clawhub.ai/user/alexanderliteplo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover people on RentAHuman.ai, create task bounties, message candidates, and manage applicant decisions for physical-world work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated actions can create bounties, messages, application decisions, payments, subscriptions, webhooks, wallet changes, or API-key changes with real-world and financial impact.

Mitigation: Require dry-run previews where available and explicit operator confirmation before any bounty, message, acceptance, payment, withdrawal, subscription, webhook, or API-key action.

Risk: Task descriptions, messages, and application requirements could solicit sensitive personal data or expose private addresses and credentials.

Mitigation: Limit requests to the minimum information needed for the task and do not ask for passwords, OTP codes, private keys, seed phrases, government IDs, bank or card details, exact home addresses, or dates of birth.

Risk: Wallet-funded or escrow-related operations may reserve or release funds and some payment actions can be irreversible.

Mitigation: Show the amount, worker, task, and funding source to the operator before proceeding, and use idempotency keys when retrying paid operations.

## Reference(s):

- [RentAHuman API Reference](references/API.md)
- [RentAHuman homepage](https://rentahuman.ai)
- [RentAHuman ClawHub skill page](https://clawhub.ai/alexanderliteplo/skills/rentahuman)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated write operations require RENTAHUMAN_API_KEY; read-only search and browsing operations can be unauthenticated.]

## Skill Version(s):

3.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
