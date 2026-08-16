## Description:

This skill runs step 2 of a patent panorama workflow, using validated search outputs to produce landscape statistics, branch-organized core patent indexes, value-signal files, and a self-contained statistical dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, patent analysts, and IP strategy teams use this skill after the search stage has produced validated `search_config.json`, `candidate_pool.csv`, and `core_recall.csv`. It generates patent landscape statistics, applicant and technology breakdowns, competitor portraits, core-patent indexes, value-signal outputs, and downstream reporting inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses configured Patsnap/Open Platform MCP authorization to access patent analytics services.

Mitigation: Install and run it only in environments where that authorization is intended and where generated local report files can be stored.

Risk: Generated statistics, value scores, legal-status signals, citation signals, and family-breadth signals may be mistaken for legal, valuation, infringement, FTO, novelty, or validity conclusions.

Mitigation: Treat outputs as analytical signals and route legal, valuation, infringement, FTO, novelty, and validity decisions to qualified human review.

Risk: Default core-patent tiers can be based on recall signals rather than per-patent legal verification.

Mitigation: Preserve the skill's recall-signal and verification labels, and run bounded fallback verification for priority branches when higher confidence is required.

Risk: Missing or stale upstream inputs can produce incomplete or misleading landscape outputs.

Mitigation: Require validated `search_config.json`, `candidate_pool.csv`, and `core_recall.csv` from step 1 before running the statistical and value-signal workflow.

Risk: Without the required MCP configuration and account authorization, the skill can provide only a framework rather than database-backed results.

Mitigation: Complete the Open Platform MCP setup and self-check before relying on live patent analytics outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-insights-stats)
- [Open Platform marketplace listing](https://open.zhihuiya.com/marketplace/skill-hub/patent-panorama-insights-stats)
- [Open Platform MCP setup](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus JSON, CSV, and self-contained HTML file specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected file outputs include panorama_stats.json, assignee_normalization.json, patent_index.core.json/.csv, value_signals.json, chart_data.json, panorama_stats_report.html, and an extended report_manifest.json when required inputs and MCP authorization are available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
