## Description: <br>
Helps agents evaluate restaurant and retail locations using structured site, traffic, competition, map-proxy, and financial inputs to produce data-driven category recommendations and decision-ready Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monsterdt](https://clawhub.ai/user/monsterdt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, operators, analysts, and developers use this skill to assess candidate restaurant or retail sites, compare trade-area strength, model payback scenarios, and generate Markdown decision reports with category-fit guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using map MCP can send a target address or coordinates to the configured map provider. <br>
Mitigation: Require explicit user consent before any map MCP call and limit outbound map-provider data to address or coordinates. <br>
Risk: Restaurant financial, compliance, and business details may be sensitive. <br>
Mitigation: Keep financials, red flags, category choices, and other business inputs local to the agent-side calculation and do not include them in map-provider requests. <br>
Risk: Location-analysis phrases can activate the skill and may lead users toward map-assisted analysis. <br>
Mitigation: Treat activation as a prompt to clarify inputs and consent; do not perform external map calls unless the user approves location sharing. <br>
Risk: Site-selection reports can be mistaken for guaranteed investment outcomes. <br>
Mitigation: Present outputs as data-driven projections, include confidence intervals and assumptions, and distinguish map proxy metrics from manual estimates or field-verified data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/monsterdt/skills/location-site-selection) <br>
- [Publisher profile](https://clawhub.ai/user/monsterdt) <br>
- [Benchmarks and formulas](references/benchmarks.md) <br>
- [Map MCP guide](references/map_mcp_guide.md) <br>
- [Example decision report](examples/decision_report_demo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with tables, ASCII visualizations, JSON result blocks, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should distinguish map-derived proxy data from manual estimates and should present confidence intervals rather than guaranteed returns.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
