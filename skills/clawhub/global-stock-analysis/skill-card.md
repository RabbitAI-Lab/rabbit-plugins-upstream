## Description: <br>
Global stock analysis for US, China, and EU markets, including technicals, fundamentals, macro data, forex, crypto, and options workflows powered by Alpha Vantage market data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luohy15](https://clawhub.ai/user/luohy15) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate terminal-based workflows for researching equities, comparing companies, reviewing technical and fundamental signals, checking macro conditions, and inspecting forex, crypto, and options data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires installing the third-party marketdata-cli package and providing an Alpha Vantage API key. <br>
Mitigation: Confirm the package source before installing, store the API key securely, and avoid committing any .env file or command history containing credentials. <br>
Risk: Market-data outputs and generated workflows may be used to support financial decisions. <br>
Mitigation: Review commands before running them and verify results with appropriate financial due diligence before acting on them. <br>


## Reference(s): <br>
- [Fundamental Analysis](references/fundamentals.md) <br>
- [Technical Analysis](references/technicals.md) <br>
- [Macro & Market Overview](references/macro.md) <br>
- [Sector / Multi-Stock Comparison](references/comparison.md) <br>
- [Forex & Crypto](references/forex-crypto.md) <br>
- [Options Chain](references/options.md) <br>
- [Alpha Vantage](https://www.alphavantage.co) <br>
- [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key) <br>
- [Installation Tutorial](https://www.youtube.com/watch?v=Z6DjYKN4uos) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; referenced CLI commands can return terminal text, CSV, or JSON depending on flags.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires marketdata-cli and an ALPHAVANTAGE_API_KEY.] <br>

## Skill Version(s): <br>
0.0.14 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
