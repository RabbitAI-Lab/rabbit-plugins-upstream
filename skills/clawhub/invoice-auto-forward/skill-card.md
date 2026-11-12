## Description:

Automatically scans invoice emails, extracts invoice data from PDF, OFD, or XML files, and forwards matching invoices to configured finance or administrative recipients with whitelist filtering, link-based invoice download, scheduling support, and send-rate controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Employees, finance operations teams, and agent operators use this skill to configure and run automated invoice forwarding from supported mailboxes. It helps preview, filter, deduplicate, and forward invoice messages to the right recipients while keeping credentials outside the skill package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs mailbox access and SMTP sending authority, which can expose sensitive invoice and account data if configured on a broad mailbox.

Mitigation: Use a dedicated invoice mailbox where possible, keep authorization codes out of chat and logs, and verify the generated secrets file permissions before unattended runs.

Risk: Unattended forwarding can send unwanted or duplicate invoice messages if filters, recipients, or state files are wrong.

Mitigation: Run the scan preview and review recipients, buyer whitelist settings, and de-duplication state before enabling scheduled run mode.

Risk: Email-controlled link fetching can retrieve content from links embedded in messages.

Mitigation: Disable link fetching when it is not needed, or configure a strict link_domains allowlist with conservative timeout and size limits.

Risk: Automatic dependency installation changes the active Python environment.

Mitigation: Use a dedicated virtual environment and install pinned dependencies manually before running check or scheduled jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/invoice-auto-forward)
- [Configuration Example](references/config.example.json)
- [Troubleshooting Guide](references/troubleshooting.md)
- [README](README.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, and script-generated text or Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime script can produce scan previews, send summaries, parsed invoice fields, persistent configuration files, credential file instructions, de-duplication state, and daily Markdown reports.]

## Skill Version(s):

1.0.9 (source: frontmatter and CHANGELOG, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
