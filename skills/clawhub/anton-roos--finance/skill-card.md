## Description: <br>
Track stocks, ETFs, indices, crypto (where available), and FX pairs with caching + provider fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anton-roos](https://clawhub.ai/user/anton-roos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch market quotes, generate stock, ETF, and index series, maintain a local watchlist, and summarize finance data with provider caveats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts public finance APIs and may be affected by provider rate limits, unofficial access changes, or delayed FX updates. <br>
Mitigation: Use caching and throttling, avoid claiming real-time data unless the selected provider supports it, and consider a paid provider for frequent or high-volume access. <br>
Risk: The skill writes local cache and watchlist state, and the documented metadata state directory differs from the script path. <br>
Mitigation: Run it in a dedicated virtual environment or workspace and review local state under .cache/market-tracker before sharing or packaging. <br>


## Reference(s): <br>
- [ClawHub finance skill](https://clawhub.ai/anton-roos/skills/finance) <br>
- [Publisher profile](https://clawhub.ai/user/anton-roos) <br>
- [Provider and symbol formats](providers.md) <br>
- [ExchangeRate-API Open Access endpoint](https://open.er-api.com/v6/latest/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with shell commands; scripts can emit JSON quotes, CSV series, and JSON watchlist summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local cache and watchlist; public finance providers may rate-limit and FX open access data updates daily.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
