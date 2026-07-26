## Description: <br>
Finance Analysis is a CLI skill for financial statement analysis, stock valuation, and risk assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, finance practitioners, and investment researchers use this skill to run CLI-based company financial analysis, DCF and relative valuation checks, and simple risk scoring from stock ticker inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Valuation, risk score, and buy-style wording may be misleading because parts of the output are illustrative or hardcoded. <br>
Mitigation: Treat outputs as analysis aids only; verify assumptions, data sources, and calculations before using results for financial decisions. <br>
Risk: The skill may use a Tushare API token for market data access. <br>
Mitigation: Store API tokens in environment variables, avoid sharing logs that expose credentials, and rotate tokens if accidental disclosure occurs. <br>
Risk: Financial analysis can become stale or incomplete if data sources are unavailable or not current. <br>
Mitigation: Confirm data freshness and compare outputs against authoritative filings or market-data providers before relying on conclusions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/finance-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/haidiantoutou) <br>
- [Project Homepage](https://github.com/alsoforever/gungun-life) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI output with Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses stock ticker inputs and an optional TUSHARE_TOKEN environment variable; outputs include financial metrics, valuation summaries, and risk scores.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
