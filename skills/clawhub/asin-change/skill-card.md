## Description:

Monitors saved Amazon ASIN product snapshots on supported daily or weekly schedules and returns deterministic change digests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to manage ARI product snapshot watches and read 7-day or 30-day ASIN field-change digests. It is intended for deterministic snapshot monitoring, not real-time price, sales, inventory, advertising, order, or return-rate tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI exposes paid AI analysis and broader account operations beyond ASIN watch digests.

Mitigation: Use only the documented watch commands, review or disable ARI auto-confirm settings, and avoid analyze, voc, operations, advise, leaderboard, workbench mutation, and export commands unless those behaviors are intentional.

Risk: The skill requires an ARI API key and authenticated account access.

Mitigation: Install only when ARI account access is acceptable, keep API keys out of prompts and logs, and verify any custom ARI endpoint settings before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-change)
- [Amazon ASIN 变化监控 专用监控参考](artifact/references/reference.md)
- [Amazon ASIN 变化监控 专用监控工作流](artifact/references/watch-workflow.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deterministic watch digest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the watch/all workflow with the watch_digest output template; digest supports 7d and 30d periods and requires an ARI API key.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
