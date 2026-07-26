## Description: <br>
独孤九剑 is an A-share short-term stock analysis skill that fetches market data, computes technical features, matches a nine-tactic rule system, and produces chart-supported trading analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yhc2026](https://clawhub.ai/user/yhc2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze A-share stock codes with a rule-based short-term trading framework, optional MCP tools, and chart generation. It is intended to provide informational market analysis, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to public market-data providers and possibly news sources. <br>
Mitigation: Enable it only in environments where those network calls are acceptable, and review provider terms before running the MCP server. <br>
Risk: Generated stock analysis may be mistaken for investment advice. <br>
Mitigation: Treat recommendations and trading levels as informational analysis that requires independent review. <br>
Risk: Runtime behavior depends on Python packages and external market-data libraries. <br>
Mitigation: Pin dependencies and review installed packages for stricter production or enterprise environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yhc2026/skills/charts) <br>
- [Framework knowledge](knowledge/framework.md) <br>
- [MCP platform configuration guide](mcp_server/PLATFORM_CONFIGS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown analysis reports, JSON MCP tool responses, shell commands, configuration snippets, and PNG chart file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May fetch public market data and generate local chart images when charting is requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
