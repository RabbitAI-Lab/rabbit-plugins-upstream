## Description:

Summarizes deterministic changes in price and primary BSR fields from saved Amazon product snapshots, with sampling times, using the fixed watch/price_bsr workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to list, create, pause, resume, delete, and summarize ARI watch jobs for saved Amazon product snapshots. It is intended for price and BSR field tracking, not real-time pricing, sales prediction, inventory, advertising, order management, or automatic repricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises a narrow price and BSR tracker, but the bundled ARI CLI can also perform broader account, paid analysis, export, and review-management actions.

Mitigation: Review before installing, keep agent use limited to the documented watch commands, and require explicit user confirmation before any paid or state-changing action.

Risk: The bundled CLI requires access to an ARI account key.

Mitigation: Use only an intentional ARI_API_KEY or local user configuration, avoid embedding keys in the skill package, and do not allow custom ARI endpoints unless the operator explicitly enables ARI_ALLOW_CUSTOM_BASE.

Risk: The watch workflow may not be available in an installed CLI version.

Mitigation: Run python scripts/ari.py watch --help before use and stop with an upgrade prompt if the watch subcommands are unavailable.

Risk: Users may confuse deterministic watch digests with AI weekly reports or real-time marketplace data.

Mitigation: State daily or weekly quota and scanning cost before creating or changing watch schedules, and route AI weekly reports through a separate explicitly confirmed workflow.

## Reference(s):

- [Amazon 价格与 BSR 变化追踪 专用监控参考](references/reference.md)
- [Amazon 价格与 BSR 变化追踪 专用监控工作流](references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON command-output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; deterministic watch digest output reports creditsUsed: 0.]

## Skill Version(s):

1.4.3 (source: server release evidence, skill frontmatter, _meta.json, and script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
