## Description: <br>
Helps an agent handle Eastmoney MX simulated A-share portfolio requests, including holdings, balances, orders, fills, explicit simulated buy or sell actions, order cancellation, and simulated trading experience posts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to query and manage an Eastmoney MX simulated A-share portfolio. It is intended for simulated trading practice only, not real-money trading, investment advice, stock screening, watchlist management, news research, or quote-only requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an MX_APIKEY to access an Eastmoney MX simulated account. <br>
Mitigation: Keep MX_APIKEY private and install the skill only when connecting Codex to the intended simulated account. <br>
Risk: Simulated buy, sell, cancel, and posting requests can mutate the simulated account or publish simulated trading content. <br>
Mitigation: Review the requested simulated action, stock code, quantity, price or market-price choice, order id, and post text before execution. <br>
Risk: Changing MX_API_URL could redirect account API calls away from the trusted default endpoint. <br>
Mitigation: Leave MX_API_URL at the trusted default unless there is a specific, reviewed reason to change it. <br>


## Reference(s): <br>
- [mx-moni API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zoeluli7459-dev/skills/mx-moni) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with command examples, formatted simulated-account summaries, and generated JSON/TXT file paths when produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs must state that results come from a simulated account and must report API status without implying success when a response is missing or failed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
