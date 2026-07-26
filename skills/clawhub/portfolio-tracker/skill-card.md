## Description: <br>
Automates live portfolio tracking and analysis using browser automation on Yahoo Finance, fetching real-time prices, updating portfolio-tracker.md, and generating performance summaries, winners and losers, rebalancing suggestions, and market news. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vachanalaviswanath](https://clawhub.ai/user/vachanalaviswanath) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to update and analyze a specific stock and crypto portfolio with live Yahoo Finance data. It supports portfolio value checks, performance summaries, concentration review, and rebalancing suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads included portfolio holdings and can update a local portfolio tracker, which may expose sensitive portfolio composition. <br>
Mitigation: Invoke it only for explicit portfolio update requests and review generated files before sharing them. <br>
Risk: Broad finance-related trigger wording can lead to Yahoo Finance browsing and local tracker edits from ambiguous requests. <br>
Mitigation: Prefer explicit commands such as "update my portfolio tracker" and confirm intended file edits before applying them. <br>


## Reference(s): <br>
- [Portfolio Holdings](references/portfolio-holdings.md) <br>
- [Yahoo Finance BTC-USD Quote](https://finance.yahoo.com/quote/BTC-USD) <br>
- [ClawHub Skill Page](https://clawhub.ai/vachanalaviswanath/skills/portfolio-tracker) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/vachanalaviswanath) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown analysis with portfolio tables, inline commands, and local file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update portfolio-tracker.md and includes live-market snapshots from Yahoo Finance.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
