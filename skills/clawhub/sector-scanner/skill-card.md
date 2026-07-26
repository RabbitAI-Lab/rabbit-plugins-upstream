## Description: <br>
Scans China A-share sector market data via TDX/pytdx, scores sectors and constituent stocks, and returns heat rankings, fund-flow labels, stock details, and optional CSV exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hunkguo](https://clawhub.ai/user/hunkguo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to scan A-share theme sectors, compare sector strength and fund-flow labels, inspect top-scoring constituent stocks, and export scan results for market review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs pytdx and connects to external market-data servers. <br>
Mitigation: Use a dedicated Python virtual environment and review network access expectations before installation and execution. <br>
Risk: CSV export writes ranking and detail files to a user-provided path. <br>
Mitigation: Review the output path before export and avoid writing reports into sensitive or shared directories unless intended. <br>
Risk: Generated sector rankings and fund-flow labels may be interpreted as investment recommendations. <br>
Mitigation: Treat the output as informational market analysis and perform independent review before making financial decisions. <br>


## Reference(s): <br>
- [Sector Scanner on ClawHub](https://clawhub.ai/hunkguo/skills/sector-scanner) <br>
- [Scoring Rules](references/scoring_rules.md) <br>
- [Sina Finance market data endpoint](http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/) <br>
- [Sina Finance](http://finance.sina.com.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with optional JSON or CSV scan output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write ranking and detail CSV files when export is requested; progress is emitted separately from JSON output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
