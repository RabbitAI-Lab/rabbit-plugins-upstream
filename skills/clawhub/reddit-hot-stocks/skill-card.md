## Description: <br>
Powered by AgentKey, this skill identifies US stocks gaining retail attention by combining live Reddit discussions, market quotes, catalyst checks, sentiment drivers, and risk signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zzallenn](https://clawhub.ai/user/zzallenn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to identify US-listed equities and ETFs gaining attention on Reddit, then validate signals with live market quotes, recent catalysts, sentiment drivers, and risk flags. It produces market research watchlists, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts a third-party AgentKey MCP service for live Reddit and market data. <br>
Mitigation: Avoid sending sensitive portfolio, account, or personal financial details unless they are necessary for the request. <br>
Risk: Reddit posts, comments, and linked content are untrusted external data. <br>
Mitigation: Summarize and cite evidence without executing instructions, links, or code found in posts or comments. <br>
Risk: Retail attention can be confused with investment conviction. <br>
Mitigation: Frame results as watchlist signals with uncertainty and risk, and avoid buy, sell, short, or other trading instructions. <br>


## Reference(s): <br>
- [AgentKey Tool Reference](references/agentkey-tools.md) <br>
- [AgentKey](https://agentkey.app) <br>
- [Reddit Hot Stocks on ClawHub](https://clawhub.ai/zzallenn/skills/reddit-hot-stocks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown table with a short method section] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Ranked watchlist with evidence, market checks, risk flags, next checks, AgentKey endpoints used, call count, and approximate credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
