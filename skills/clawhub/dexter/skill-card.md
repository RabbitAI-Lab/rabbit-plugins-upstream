## Description: <br>
Autonomous financial research agent for stock analysis, financial statements, metrics, prices, SEC filings, and crypto data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[igorhvr](https://clawhub.ai/user/igorhvr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and analysts use Dexter to answer financial research questions about stocks, crypto, company fundamentals, SEC filings, analyst estimates, insider trades, and market news. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill clones, installs, patches, and runs an external Dexter project before use. <br>
Mitigation: Review the upstream project and dependencies before running bun install or executing generated scripts. <br>
Risk: Dexter uses API keys and may send financial research prompts to third-party providers. <br>
Mitigation: Use least-privilege API keys, keep .env private, and avoid confidential research unless those providers are acceptable. <br>
Risk: Financial data coverage is strongest for US stocks and fallback web search can vary in reliability. <br>
Mitigation: Check important financial outputs against primary filings, market data providers, or other trusted sources before acting on them. <br>


## Reference(s): <br>
- [ClawHub Dexter skill page](https://clawhub.ai/igorhvr/skills/dexter) <br>
- [Financial Datasets API](https://financialdatasets.ai) <br>
- [Tavily web search](https://tavily.com) <br>
- [Anthropic Console](https://console.anthropic.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and TypeScript code blocks, plus financial research answers from Dexter runs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bun and git on Darwin or Linux, plus API keys for an LLM provider and financial data; Tavily is optional for web search fallback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
