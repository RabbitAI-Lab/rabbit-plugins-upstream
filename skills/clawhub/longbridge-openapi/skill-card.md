## Description: <br>
Longbridge Openapi helps agents use Longbridge Securities tooling for market data, portfolio and account lookups, analysis workflows, watchlists, price alerts, and recurring DCA plan operations across US, HK, CN, SG, and crypto markets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[genkin-he](https://clawhub.ai/user/genkin-he) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer finance, market, portfolio, and trading workflow questions through Longbridge CLI or MCP-backed tools. Authenticated account workflows support private account state, watchlist administration, price alerts, and recurring DCA plan management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated Longbridge workflows can expose sensitive account details such as holdings, orders, cash flow, statements, watchlists, alerts, and DCA plans. <br>
Mitigation: Show private account values only in direct conversation and avoid copying them into tickets, pull requests, logs, or other shared artifacts. <br>
Risk: Watchlist administration, price alerts, and recurring DCA plans can change persistent account state; DCA plans can commit real money on a schedule. <br>
Mitigation: Use the skill's preview-then-confirm protocol, require explicit confirmation for mutations, read back all DCA parameters, and do not silently retry failed mutating calls. <br>
Risk: Financial analysis and market summaries may be misunderstood as investment advice. <br>
Mitigation: Cite Longbridge Securities as the data source, keep conclusions grounded in retrieved data, and include the skill's investment-risk disclaimer in analysis sections. <br>
Risk: Connecting the skill requires Longbridge credentials or OAuth access and may grant access to account-scoped capabilities. <br>
Mitigation: Install only when intending to connect the agent to a Longbridge account, confirm requested credentials and scopes, and avoid account-changing actions unless the preview exactly matches the user's request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/genkin-he/skills/longbridge-openapi) <br>
- [Longbridge skills homepage](https://github.com/longbridge/skills) <br>
- [Longbridge OpenAPI documentation](https://open.longbridge.com) <br>
- [Longbridge llms.txt](https://open.longbridge.com/llms.txt) <br>
- [Longbridge MCP endpoint](https://openapi.longbridge.com/mcp) <br>
- [Longbridge terminal](https://github.com/longportapp/longbridge-terminal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI or MCP command workflows, JSON-backed result summaries, and optional generated files such as DOCX or CSV exports when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should match the user's language and include Longbridge source attribution and investment-risk disclaimers for analysis sections.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
