## Description:

Generates sports event overview reports across football, basketball, NBA, Premier League, Chinese Super League, UEFA Champions League, and other sports by organizing public match information into visual, source-aware viewing aids without result predictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External sports fans, commentators, educators, and developers use this skill to gather public match context, produce daily or single-match viewing reports, and visualize formations, players, data panels, and source-graded pre-match information without result predictions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run Python scripts, fetch public sports data, read API keys from environment variables, and write report or data files.

Mitigation: Install only where those behaviors are expected, restrict API-key and file-write access as needed, and review generated files before sharing.

Risk: Generic URL fetching and daily automation can broaden data ingestion and execution scope.

Mitigation: Disable or restrict generic --url fetching and require explicit opt-in before enabling daily automation.

Risk: In-place dataset mutation and avatar or gender heuristics can affect authoritative datasets or introduce sensitive assumptions.

Mitigation: Avoid --write-gender and in-place --fix on authoritative datasets, and review generated reports for sensitive avatar assumptions.

Risk: Generated reports may include promotional sections or stale sports context.

Mitigation: Review generated reports for promotional content, freshness markers, and factual accuracy before broad use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/sports-data-analysis)
- [README](artifact/README.md)
- [Report input template](artifact/assets/report_template.md)
- [Analysis methodology](artifact/references/analysis_methodology.md)
- [Data sources and collection tiers](artifact/references/data_sources.md)
- [Daily update workflow](artifact/references/daily_update_workflow.md)
- [Professional analysis dimensions](artifact/references/professional_analysis.md)
- [Risk and compliance guidance](artifact/references/risk_compliance.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML files, JSON configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated self-contained HTML reports and JSON data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include source and freshness markers, report previews, local report files, and updated match data.]

## Skill Version(s):

2.10.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
