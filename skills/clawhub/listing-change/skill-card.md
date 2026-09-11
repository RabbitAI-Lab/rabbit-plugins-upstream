## Description:

Uses saved Amazon product snapshots and deterministic diffs to alert users when listing fields such as titles, bullets, and images change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and support agents use this skill to create, manage, and read listing-change watches for ASINs from saved product snapshots. It is intended for listing-change alerts, not real-time monitoring, sales or inventory inference, or automated listing edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is presented as a narrow listing-change watcher, but the bundled CLI exposes broader authenticated ARI account, paid analysis, export, and auto-confirm controls.

Mitigation: Review before installing; use a scoped API key or watch-only build if available, and execute only the watch commands needed for the listing-change workflow.

Risk: The skill requires an ARI API key and sends authenticated requests to the ARI service.

Mitigation: Prefer a least-privilege key, avoid untrusted custom service endpoints, and rotate or revoke the key if the package or runtime environment is no longer trusted.

Risk: The documentation marks the watch workflow as planned and requires confirming that the current CLI exposes watch subcommands.

Mitigation: Run `python scripts/ari.py watch --help` before use and stop if the watch subcommands are unavailable instead of falling back to another workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/listing-change)
- [Amazon Listing 变化提醒 专用监控参考](references/reference.md)
- [Amazon Listing 变化提醒 专用监控工作流](references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; watch digests are documented as deterministic and zero-credit, while other bundled CLI commands may access broader ARI account features.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
