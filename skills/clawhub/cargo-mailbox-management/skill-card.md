## Description:

Send mail from Cargo-owned inboxes by provisioning mailboxes, running provider warm-up and send-ramp checks, delivering with the `sendEmail` action, and reading threads, replies, delivery events, and suppression-list state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to manage Cargo mailboxes for outbound email operations, including provisioning, warm-up, allowance checks, live sends, reply tracking, and workspace-wide suppression handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing and running an unpinned `@cargo-ai/cli` while using authenticated mailbox authority.

Mitigation: Use a pinned reviewed Cargo CLI version, confirm the active workspace with `cargo-ai whoami`, and verify token permissions before running mailbox write operations.

Risk: CLI sends are live and there is no dry-run flag for `orchestration action execute`.

Mitigation: Send to a controlled internal address first, inspect the rendered email, and check `mailbox get-send-allowance` before enrolling a batch.

Risk: Provisioning mailboxes creates recurring monthly credit charges.

Mitigation: Run `pricing get`, quote the mailbox count and monthly credit estimate, and obtain explicit approval before creating mailboxes.

Risk: Outbound email can contact suppressed or unsuitable recipients if the operator skips the documented gates.

Mitigation: Run basis, suppression, and relevance checks before sending, and treat workspace-wide suppressions as absolute.

## Reference(s):

- [Cargo Skill Release](https://clawhub.ai/cargo-ai/skills/cargo-mailbox-management)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Mailbox recipes](references/examples/recipes.md)
- [Response shapes and enums](references/response-shapes.md)
- [Sending: the `sendEmail` action](references/sending.md)
- [Troubleshooting](references/troubleshooting.md)
- [Warm-up and the send ramp](references/warmup-and-allowance.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live Cargo CLI commands that can provision paid mailboxes or send real email when executed by an authenticated user.]

## Skill Version(s):

1.0.3 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
