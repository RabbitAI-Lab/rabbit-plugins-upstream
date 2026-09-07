## Description:

Amazon Listing 健康检查 checks Amazon ASIN listing completeness, misunderstanding risks, and review-backed evidence for listing health diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and ecommerce teams use this skill to inspect an ASIN's listing health, check whether product and review evidence are sufficient, and receive concise issue summaries and operational guidance. The skill is scoped to listing health diagnostics and excludes full listing copywriting, advertising bid work, inventory, order, and profit analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader ARI account actions than a narrow listing-health description may imply, including review analysis, reports, exports, monitoring, and persistent account settings.

Mitigation: Install only when ARI account-level access for these actions is intended, and review the enabled workflows before use.

Risk: Some collection, analysis, and monitoring workflows can consume ARI credits, and account auto-confirm settings may allow small paid actions to run without a separate prompt.

Mitigation: Use quote-only flows for price checks, review auto-confirm billing settings, and require explicit approval for recurring monitoring or competitor binding.

Risk: Exports write report or review data to local paths and may overwrite existing files if paths are chosen carelessly.

Mitigation: Choose export destinations deliberately and verify paths before running export commands.

Risk: Interrupted streams may have already completed and consumed credits on the server, so immediate retries can duplicate paid work.

Mitigation: Check report or operation status using the original request identifiers before retrying any paid command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/listing-health)
- [ARI Service](https://ari.funewa.com)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [Listing Health Operations Workflow](artifact/references/operation-workflow.md)
- [User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text with optional shell commands, JSON-derived report summaries, exported files, and ARI web report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish direct data, inference, and strategy advice; paid operations require quote and confirmation behavior according to the ARI service response.]

## Skill Version(s):

1.4.7 (source: server release metadata, target metadata, frontmatter, changelog, _meta.json, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
