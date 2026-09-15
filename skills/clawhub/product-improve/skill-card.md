## Description:

Transforms Amazon review complaints into prioritized product improvement actions and supports ARI review collection, VOC and insight reports, competitor comparison, product monitoring, alert/workbench workflows, and report or CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product operators, and agents use this skill to turn review data into concise product improvement priorities, quality issue summaries, listing suggestions, monitoring decisions, and exportable reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and sends ASINs, review/report requests, and account-scoped actions to ari.funewa.com.

Mitigation: Install only if this data sharing is acceptable, use ARI authorization rather than pasting secrets into chat, and revoke or rotate the key if access is no longer needed.

Risk: Paid analysis, leaderboard lookup, collection, and advice workflows can spend account credits, including cases governed by auto-confirm rules.

Mitigation: Use "only quote, do not execute" for estimates and request confirmation before every credit deduction when reviewing or operating the skill.

Risk: Auto-confirm settings, schedules, watches, competitor tracking, exports, and workbench status changes can alter persistent account state or write local export files.

Mitigation: Require explicit user intent for these actions, verify target ASINs or watch IDs, and review export paths before execution.

Risk: Product recommendations can be misleading when based on small, stale, or partially collected review samples.

Mitigation: Include sample size, date range, collection window, and unavailable data notes, and avoid presenting inferred trends as facts when evidence is insufficient.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/product-improve)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [Usage Guide](使用说明.md)
- [ARI CLI and API Reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown, text summaries, JSON-backed CLI results, and optional CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope, sample limitations, actual usage or credits when returned, and report links when available.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, artifact frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
