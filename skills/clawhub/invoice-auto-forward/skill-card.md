## Description:

Automatically scans authorized mailboxes for invoice emails, parses PDF/OFD/XML invoices, filters them by buyer name, and forwards matching invoice documents to configured recipients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Employees, finance teams, and administrative users use this skill to set up mailbox-based invoice forwarding workflows. It helps an agent configure credentials, preview candidate invoices, run forwarding jobs, and explain run reports without exposing mail authorization codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access mailboxes and forward financial documents automatically.

Mitigation: Install it only for mailboxes the user is authorized to process, and verify forwarding recipients and buyer whitelist behavior with `scan` before running unattended forwarding.

Risk: Link-based invoice handling can fetch URLs found in email content.

Mitigation: Use a strict `link_domains` allowlist or disable `fetch_links`; keep timeout and maximum-byte limits enabled.

Risk: Configuration, state, and generated reports may contain sensitive business metadata.

Mitigation: Store generated files in a protected local directory and avoid sharing reports, state files, or authorization-code details in chat or logs.

Risk: Skipping connection verification can leave invalid mailbox credentials or forwarding settings in place.

Mitigation: Avoid `--no-verify` except for deliberate offline testing, and run `check` before scheduled or batch use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/invoice-auto-forward)
- [Configuration example](references/config.example.json)
- [Troubleshooting guide](references/troubleshooting.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, Text]

**Output Format:** [Markdown guidance with shell commands, configuration paths, and run-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or explain local configuration, state, and daily report files for invoice forwarding workflows.]

## Skill Version(s):

1.0.9 (source: frontmatter, CHANGELOG released 2026-09-05, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
