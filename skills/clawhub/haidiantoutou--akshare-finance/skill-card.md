## Description: <br>
Akshare Finance wraps AKShare financial data APIs for stocks, futures, options, funds, foreign exchange, bonds, indexes, cryptocurrency, macroeconomic, real-time, historical, and derived market data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to fetch public financial market and macroeconomic data through AKShare, generate example Python calls, and inspect returned tabular data. It is not investment advice; users should verify important data independently. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial market data may be delayed, incomplete, or inaccurate. <br>
Mitigation: Verify important financial data against authoritative sources before using it for trading, reporting, or business decisions. <br>
Risk: The skill installs AKShare and pandas from PyPI and fetches public market data. <br>
Mitigation: Install dependencies in a managed Python environment and apply normal dependency review and network-use controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/akshare-finance) <br>
- [AKShare documentation](https://akshare.akfamily.xyz/) <br>
- [AKShare GitHub repository](https://github.com/akfamily/akshare) <br>
- [AKShare reference guide](references/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, json] <br>
**Output Format:** [Markdown guidance with Python and shell examples; helper scripts print JSON and AKShare functions commonly return Pandas DataFrames.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires akshare>=1.12 and pandas>=1.5; financial data comes from public sources and may be delayed or inaccurate.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
