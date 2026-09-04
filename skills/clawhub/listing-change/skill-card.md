## Description:

Tracks saved Amazon listing snapshots and deterministic diffs to alert users when supported product-page fields such as titles, bullet points, and images change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and developers use this skill to list, create, pause, resume, delete, and review daily or weekly listing-change watches for saved ASIN snapshots. It is intended for deterministic snapshot-change alerts, not real-time monitoring, page modification, or sales, inventory, order, advertising, or return-rate analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged CLI exposes broader paid AI, review, export, and operations workflows beyond the advertised listing-change watcher.

Mitigation: Restrict agent use to python scripts/ari.py watch ... commands for this skill and require separate confirmation before using paid AI or non-watch workflows.

Risk: The ARI CLI may store or use an ARI API key locally when setup or configure workflows are used.

Mitigation: Avoid setup/configure unless local key storage is intended, and review ARI account permissions and auto-confirm settings before installation or use.

## Reference(s):

- [Amazon Listing 变化提醒 专用监控参考](artifact/references/reference.md)
- [Amazon Listing 变化提醒 专用监控工作流](artifact/references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/listing-change)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown with inline shell commands and watch-digest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses watch/listing and watch_digest; deterministic digest reports creditsUsed: 0 according to artifact documentation.]

## Skill Version(s):

1.4.5 (source: frontmatter, _meta.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
