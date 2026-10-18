## Description:

Helps agents provision and warm up Cargo sending mailboxes, check send allowances, send email, and review replies, delivery events, and suppressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents managing Cargo outbound email use this skill to provision mailboxes, monitor warm-up and sending capacity, send messages, and handle replies and opt-outs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unpinned CLI gives its package access to the Cargo workspace and live mailbox operations.

Mitigation: Review and pin a trusted CLI version before installation; confirm the active workspace before writes.

Risk: Mailbox provisioning incurs recurring monthly charges, and sends or deletion change live operations.

Mitigation: Check live pricing and obtain explicit approval for recurring costs before provisioning; review recipients and effects before sending or deleting.

Risk: Cargo credentials and returned mailbox credentials may be exposed in logs or screenshots.

Mitigation: Keep credential files and returned mailbox credentials out of logs, screenshots, and shared responses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-mailbox-management)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Mailbox recipes](references/examples/recipes.md)
- [Warm-up and send allowance](references/warmup-and-allowance.md)
- [Sending guidance](references/sending.md)
- [Sending domains](references/sending-domains.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with inline shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries of mailbox status, sending capacity, replies, and recurring costs.]

## Skill Version(s):

1.3.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
