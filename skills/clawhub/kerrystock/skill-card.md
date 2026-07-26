## Description: <br>
Kerrystock guides agents through calendar-effect and seasonality analysis for stocks, ETFs, and funds, including historical data export, cross-checks, buy/sell timing, report generation, and screening with technical signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caoshun-sudo](https://clawhub.ai/user/caoshun-sudo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and finance-oriented agent users use this skill to analyze a single security or fund's monthly and annual seasonality and produce a trade-plan style report. It can also guide combined seasonality and technical-indicator screening, with outputs treated as analysis rather than investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated buy and sell timing may be mistaken for investment advice or may overstate historical seasonality. <br>
Mitigation: Treat outputs as analysis only, include the skill's risk notice, and review decisions against the user's risk tolerance and current market context. <br>
Risk: Configurable local tool paths could run an unintended script if environment variables are untrusted. <br>
Mitigation: Use trusted values for NODE_BIN, PYTHON_BIN, WESTOCK_DATA_SCRIPT, NEODATA_SCRIPT, and WB_FINANCE_QUANT_DIR before running commands. <br>
Risk: Short histories, sparse monthly samples, or fund data limitations can make seasonal conclusions unreliable. <br>
Mitigation: Check the reported sample count n, flag low-sample months, and cross-check calculated seasonality with independent data where available. <br>
Risk: The neodata verification flow uses a temporary token for external data access. <br>
Mitigation: Pass only a fresh temporary token at runtime and avoid persisting credentials in generated reports or configuration. <br>


## Reference(s): <br>
- [Kerrystock ClawHub skill page](https://clawhub.ai/caoshun-sudo/skills/kerrystock) <br>
- [Workflow reference](references/workflow.md) <br>
- [Lessons learned](references/lessons.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, plus generated CSV, JSON, and HTML report files when scripts are run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces financial analysis artifacts from local market-data tools; outputs are analytical and not investment advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
