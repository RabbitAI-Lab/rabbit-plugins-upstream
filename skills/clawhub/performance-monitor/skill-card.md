## Description: <br>
Performance Monitor helps agents build source-tagged SEO/GEO performance reports and configure ranking, traffic, backlink, technical, competitor, and AI-visibility alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, SEO, GEO, and engineering stakeholders use this skill to generate period-over-period performance reports or set up monitoring alerts for organic traffic, rankings, authority, backlinks, technical health, competitor movement, and AI visibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may summarize SEO, traffic, ranking, backlink, competitor, and alert-routing information when tools are connected or exports are provided. <br>
Mitigation: Confirm the intended domain, mode, reporting period or alert baseline, and save location before allowing data reads or monitoring-memory writes. <br>
Risk: Reports or alerts can mislead users if estimates, missing inputs, or plausible explanations are presented as measured facts. <br>
Mitigation: Label every figure as Measured, User-provided, or Estimated; mark missing data as N/A or Not yet evaluated; and separate observed changes from unverified causes. <br>
Risk: Alert thresholds can be arbitrary without a baseline or normal-volatility reference. <br>
Mitigation: Require a measured or user-provided baseline when available, or clearly label default thresholds as Estimated and tune them after observed false positives or missed issues. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/performance-monitor) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Report Output Templates](artifact/references/report-output-templates.md) <br>
- [KPI Definitions](artifact/references/kpi-definitions.md) <br>
- [Report Templates by Audience](artifact/references/report-templates.md) <br>
- [Alert Configuration Templates](artifact/references/alert-configuration-templates.md) <br>
- [Alert Threshold Guide](artifact/references/alert-threshold-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, shell commands] <br>
**Output Format:** [Markdown reports, alert-configuration summaries, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires source-tagged metrics; unavailable inputs should be marked N/A or Not yet evaluated.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
