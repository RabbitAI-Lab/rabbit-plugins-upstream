## Description:

Helps agents manage Cargo-owned outbound mailboxes, including provisioning, warm-up, send allowance checks, live sending guidance, thread and event review, and workspace suppression lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo outbound mailboxes, warm-up state, send limits, message activity, replies, delivery events, and suppression records from the Cargo CLI. It is intended for workspaces that already have appropriate Cargo access and approval to operate live outbound email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through live outbound email sending and mailbox provisioning in a Cargo workspace.

Mitigation: Confirm the active workspace, use least-privilege Cargo credentials, and get explicit approval before creating recurring-cost mailboxes or sending live email.

Risk: Mailbox provisioning creates recurring monthly credit charges.

Mitigation: Check live pricing and obtain approval for fleet size and monthly cost before provisioning; remove unused mailboxes to stop billing.

Risk: Open tracking, click tracking, replies, unsubscribe events, and suppression-list data can be privacy-sensitive.

Mitigation: Treat tracking and suppression data as sensitive, respect workspace-wide suppressions, and do not route around unsubscribe decisions.

Risk: A failed basis, suppression, or relevance check can make an outbound send inappropriate.

Mitigation: Run the documented basis, suppression, and relevance checks before sending, and stop for human review when any check fails.

## Reference(s):

- [Cargo Mailbox Management Skill](https://clawhub.ai/cargo-ai/skills/cargo-mailbox-management)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Mailbox Recipes](references/examples/recipes.md)
- [Response Shapes and Enums](references/response-shapes.md)
- [Sending: the sendEmail Action](references/sending.md)
- [Troubleshooting](references/troubleshooting.md)
- [Warm-up and the Send Ramp](references/warmup-and-allowance.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides live Cargo CLI operations and summarizes command outputs for human review.]

## Skill Version(s):

1.0.1 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
