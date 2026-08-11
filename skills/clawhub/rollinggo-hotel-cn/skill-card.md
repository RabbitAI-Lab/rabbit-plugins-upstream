## Description:

RollingGo hotel booking assistant helps users search, compare, check real-time room prices, and prepare hotel bookings through RollingGo hotel services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamtzlong](https://clawhub.ai/user/dreamtzlong)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel assistants use this skill to find accommodations, compare hotels and room rates, and prepare hotel bookings after explicit user confirmation.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Installer and upgrade flows can pull and run the latest RollingGo CLI from npm or GitHub without integrity checks.

Mitigation: Install only from trusted RollingGo sources, review or pin the CLI where possible, and verify downloaded binaries before execution.

Risk: The skill can collect guest names and email addresses and guide actions that create real hotel bookings or payment links.

Mitigation: Require explicit user confirmation before price locking, order creation, and payment-link handling; enter personal information only when the user intends to book.

Risk: Hotel search prices are reference prices and locked booking references expire after a short window.

Mitigation: Reconfirm real-time price, cancellation policy, dates, guest details, and total amount before creating an order, and re-lock pricing after expiration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dreamtzlong/skills/rollinggo-hotel-cn)
- [CLI parameter reference](references/cli-params.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries for hotel search, room rates, and booking steps, with shell commands used for local CLI setup and invocation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hotel images and payment links returned by RollingGo services; internal command details and booking identifiers are intended to be hidden from end users.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
