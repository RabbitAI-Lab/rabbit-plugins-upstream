## Description:

采集并分析指定 Amazon ASIN 的 1-3 星评论，拆解差评根因、趋势、竞品差异和改进建议，并可导出评论或报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and support teams use this skill to analyze negative reviews, identify repeat complaint themes, compare competitors, monitor review changes, and turn ARI-collected review data into product, listing, and support actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to an ARI account and stores or reads an ARI API key locally.

Mitigation: Use the documented browser authorization or ARI_API_KEY flow, never share passwords or API keys in chat, and keep requests on the official https://ari.funewa.com endpoint.

Risk: Paid collection, VOC, analysis, leaderboard, operations, or advise workflows can consume ARI credits, sometimes through account auto-confirm rules.

Mitigation: Check the account's auto-confirm setting, use 'only quote, do not execute' for pricing-only requests, and require explicit confirmation when the CLI returns confirmationRequired.

Risk: Interrupted paid workflows may already have completed and charged credits before the local session sees an error.

Mitigation: Query existing reports or operation status before retrying a paid command, and retry with --confirm only after confirming no result was created.

Risk: Monitoring, competitor binding, workbench updates, and export commands can change account state or write local files.

Mitigation: Run state-changing commands only after the user asks for that specific action, and review export destination and contents before sharing files.

Risk: Review conclusions depend on ARI-collected samples and may not cover every Amazon review, variant, or recent trend.

Mitigation: State the sample scope, collection window, and trend limitations in outputs, and avoid presenting missing or low-sample data as definitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bad-review)
- [ARI CLI and API reference](references/reference.md)
- [ARI user guide](使用说明.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis, JSON-style CLI responses, report links, shell commands, and optional CSV/Markdown/HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include sampled review scope, issue frequencies, trend caveats, ARI credit usage, report IDs, report URLs, and local export paths.]

## Skill Version(s):

1.4.13 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
