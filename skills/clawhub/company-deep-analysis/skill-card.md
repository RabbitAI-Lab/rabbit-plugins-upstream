## Description: <br>
Analyzes A-share and Hong Kong-listed companies from data collection through company profile, industry structure, moat, financial, and relative valuation work, producing a Markdown deep-analysis report and an HTML investment brief. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pm2-567](https://clawhub.ai/user/pm2-567) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users such as individual investors, investment managers, industry researchers, and advisors use this skill to screen A-share and Hong Kong listed companies, generate focused company or financial analyses, and prepare deep research reports and investment briefs. <br>

### Deployment Geography for Use: <br>
Global; analysis coverage is limited to A-share and Hong Kong listed companies. <br>

## Known Risks and Mitigations: <br>
Risk: Company names, stock codes, and research queries may be sent to public finance or search providers during data collection and fallback lookup. <br>
Mitigation: Use the skill for public-company research and avoid sensitive unpublished company names or confidential deal context when query disclosure matters. <br>
Risk: The skill writes temporary market-data JSON and local report files during normal operation. <br>
Mitigation: Run it in a workspace where local file creation is expected, review generated files before sharing, and clean temporary data when reports are complete. <br>
Risk: Generated valuation and investment commentary may be incomplete, stale, or unsuitable as direct investment advice. <br>
Mitigation: Treat outputs as research support, verify key figures against current filings or trusted data providers, and require human investment review before decisions. <br>
Risk: The workflow depends on Python packages and public data endpoints that can change or fail. <br>
Mitigation: Keep dependencies updated and rerun or cross-check the analysis when data quality is degraded or a provider fallback is used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pm2-567/skills/company-deep-analysis) <br>
- [AI internal rules](references/ai-internal-rules.md) <br>
- [Financial analysis guide](references/financial-analysis-guide.md) <br>
- [Moat analysis framework](references/moat-analysis-framework.md) <br>
- [Porter five forces template](references/porter-five-forces-template.md) <br>
- [Valuation methods](references/valuation-methods.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, HTML, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, HTML briefs, JSON data files, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local report files and temporary market-data JSON; requires Python dependencies for scripted data collection.] <br>

## Skill Version(s): <br>
1.0.11 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
