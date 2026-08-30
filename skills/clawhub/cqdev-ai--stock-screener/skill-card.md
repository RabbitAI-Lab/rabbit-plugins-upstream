## Description: <br>
Stock Screener filters user-provided CSV stock data with technical, fund-flow, and fundamental factors, then ranks, scores, summarizes, and correlates candidates for downstream trading-plan workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to screen stock CSV datasets, rank candidate pools, inspect a single stock's factor score, summarize datasets, and explore factor correlations before preparing trading-plan inputs. Outputs are analysis aids only and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads CSV files explicitly passed to it, which may contain sensitive financial or portfolio data. <br>
Mitigation: Use non-sensitive copies where possible and pass only the intended CSV file paths. <br>
Risk: CSV output paths can overwrite files if chosen carelessly. <br>
Mitigation: Choose explicit output paths in a safe working directory and review generated files before relying on them. <br>
Risk: Screening scores and rankings can be misleading if input data is stale, incomplete, or unsuitable for the chosen factors. <br>
Mitigation: Verify input data quality and treat results as auxiliary analysis, not investment advice. <br>
Risk: Security guidance notes that several advertised commands may need bug fixes before they work reliably. <br>
Mitigation: Smoke-test the needed commands with representative sample CSVs before using the skill in a repeatable workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/cqdev-ai/skills/stock-screener) <br>
- [README](README.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [Skill Definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, terminal text, and optional CSV result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on user-provided CSV files and may write CSV outputs when an output path is supplied.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
