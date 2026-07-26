## Description: <br>
Financial data research via PlusE API for stock fundamentals, options analysis, market sentiment, institutional activity, insider trades, financial statements, macroeconomic data, ML price predictions, and market news. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wanghsinche](https://clawhub.ai/user/wanghsinche) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to retrieve PlusE financial data and synthesize market, company, options, sentiment, and macroeconomic research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker symbols, market research requests, and related query context are sent to PlusE using PLUSEFIN_API_KEY. <br>
Mitigation: Avoid confidential portfolio details or proprietary investment research unless the user trusts PlusE's handling of that data. <br>
Risk: Financial analysis, options research, and ML forecasts may be incomplete, stale, or unsuitable as investment advice. <br>
Mitigation: Treat outputs as research inputs and verify material conclusions against independent data and applicable compliance requirements before acting. <br>
Risk: The skill requires an API key in the PLUSEFIN_API_KEY environment variable. <br>
Mitigation: Use the key only in trusted environments and avoid exposing it in logs, shared transcripts, or shell history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wanghsinche/skills/plusefin-analysis) <br>
- [PlusE skill homepage](https://github.com/plusefin/plusefin-skill) <br>
- [PlusE API key console](https://console.plusefin.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown research reports with inline CLI, curl, and MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PLUSEFIN_API_KEY and sends financial query context to the PlusE API.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
