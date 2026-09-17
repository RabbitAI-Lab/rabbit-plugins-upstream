## Description:

Guides an agent through Cargo mailbox management: provisioning sending mailboxes, running warm-up and send-ramp checks, sending via `sendEmail`, and reading threads, replies, delivery events, pricing, and suppressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo-owned outbound mailboxes, including setup, warm-up, send allowance checks, live sending, reply/event review, suppression handling, troubleshooting, and cost-aware mailbox retirement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live outbound email operations and mailbox provisioning that affect recipients, domain reputation, and billing credits.

Mitigation: Use it only with a trusted Cargo workspace, confirm the active workspace, review proposed commands, check basis, suppression, relevance, allowance, and pricing before provisioning or sending.

Risk: The install metadata uses an unpinned `@cargo-ai/cli@latest` npm package.

Mitigation: Prefer an exact vetted Cargo CLI version for production or controlled environments.

Risk: Domain lookup guidance references a local credentials file containing bearer-token material.

Mitigation: Avoid manually reading or copying tokens from `credentials.json`; use the Cargo CLI, web app, CDK, or a narrowly scoped short-lived token for domain lookup workarounds.

Risk: The CLI path for `sendEmail` has no dry-run flag, so a proposed send can deliver real mail immediately.

Mitigation: Send to an internal or self-owned address first, inspect the rendered message, and require human review before sending to external recipients.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Mailbox recipes](references/examples/recipes.md)
- [Response shapes and enums](references/response-shapes.md)
- [Sending domains](references/sending-domains.md)
- [Sending: the `sendEmail` action](references/sending.md)
- [Troubleshooting](references/troubleshooting.md)
- [Warm-up and the send ramp](references/warmup-and-allowance.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and concise result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live Cargo CLI commands that can create mailboxes, send email, read events, or update suppressions; users should review commands before execution.]

## Skill Version(s):

1.2.0 (source: frontmatter, artifact metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
