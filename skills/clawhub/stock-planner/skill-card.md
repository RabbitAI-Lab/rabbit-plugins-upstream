## Description: <br>
Stock Planner generates next-trading-day buy, hold, stop-loss, take-profit, position-sizing, and risk-control guidance from local stock holding data and market-state inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and investors use this skill to turn CSV holdings data, cash, capital, and a market-state setting into a local trading plan with per-position profit/loss checks, stop-loss and take-profit flags, portfolio allocation guidance, correlation analysis, and leverage-risk review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-supplied holdings, price, or plan files that may contain sensitive portfolio information. <br>
Mitigation: Use explicit local file paths, share only the files needed for the analysis, and avoid storing generated plans where unauthorized users can access them. <br>
Risk: The output is trading-risk guidance and may not match the user's financial situation or current market conditions. <br>
Mitigation: Treat generated plans as informational analysis, verify input prices and timestamps, and have a qualified human review decisions before trading. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Terminal text tables and optional JSON plan files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-supplied CSV or JSON files locally and writes a JSON plan only when an output path is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, package.json, CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
