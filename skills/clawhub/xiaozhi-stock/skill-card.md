## Description: <br>
小智A股分析引擎 provides A-share market lookup, stock analysis, market sentiment review, sector scanning, quantitative screening, trading strategy guidance, stock-pool management, and real-time monitoring alerts using multiple public data sources and structured scoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[badboy2021123](https://clawhub.ai/user/badboy2021123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to retrieve Chinese equity market data, produce formatted stock and market analysis, screen candidate stocks, manage watchlists, and generate monitoring alerts. Outputs should be reviewed as informational market analysis rather than personalized financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores portfolio, watchlist, report, alert, or monitoring state data locally. <br>
Mitigation: Review the configured workspace paths and stored files before deployment, and avoid entering sensitive portfolio details unless local storage is acceptable. <br>
Risk: The skill describes scheduled or external notification flows. <br>
Mitigation: Review or disable notification behavior unless recipients, schedules, and message content are explicit and approved. <br>
Risk: Trading signals and stock recommendations can be mistaken for personalized financial advice. <br>
Mitigation: Present outputs as informational analysis, preserve the risk disclaimer, and require human review before investment decisions. <br>
Risk: Security review marked the release suspicious because some documentation describes read-only behavior while the skill can write local monitoring and portfolio files. <br>
Mitigation: Resolve the documentation mismatch and verify file-writing behavior before production rollout. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/badboy2021123/skills/xiaozhi-stock) <br>
- [README](README.md) <br>
- [Analysis methods reference](references/analysis-methods.md) <br>
- [Data sources reference](references/data-sources.md) <br>
- [Technical timing reference](references/technical-timing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis and formatted stock cards, with optional JSON or shell command output from bundled scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local stock-pool, report, alert, or monitoring state files when monitoring or portfolio features are used.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
