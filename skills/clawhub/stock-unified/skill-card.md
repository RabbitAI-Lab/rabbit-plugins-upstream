## Description: <br>
Stock Unified provides a unified Python interface for querying A-share realtime quotes, K-line history, sector rankings and constituents, financial data, sector search, and related market data across multiple public data sources with automatic fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent workflows use this skill to install and run Python market-data commands for stock quotes, historical K-line data, sector analysis, financial data, market breadth, capital-flow, futures, and index checks. Treat returned market data as informational rather than investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs Python packages and makes outbound requests to public financial-data services. <br>
Mitigation: Install only in environments where those dependencies and outbound network calls are acceptable. <br>
Risk: Returned stock and market data may be delayed, unavailable, or different across providers. <br>
Mitigation: Treat results as informational, verify important values against authoritative market sources, and avoid using the output as investment advice. <br>
Risk: The CLI includes market-data commands beyond the A-share features emphasized in the main description. <br>
Mitigation: Review the available CLI options before deployment and document any enabled commands that matter for the intended workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/stock-unified) <br>
- [Data Sources Reference](references/data_sources.md) <br>
- [Eastmoney Datacenter API Endpoint](https://datacenter.eastmoney.com/api/data/v1/get) <br>
- [Eastmoney Data Portal](https://data.eastmoney.com/) <br>
- [Sina Finance Quote Endpoint](https://hq.sinajs.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, Python examples, tabular terminal output, and optional JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python dependencies and outbound requests to public financial-data services.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
