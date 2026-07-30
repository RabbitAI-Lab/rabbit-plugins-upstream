## Description: <br>
Tracks whether fresh market news, price data, and fundamentals strengthen, weaken, falsify, realize, or leave unchanged an existing finance or investment signal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance analysts and investment researchers use this skill to update an existing market thesis against newer events, prices, and fundamentals. It helps classify the signal as strengthened, weakened, falsified, realized, or unchanged while separating facts from inference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact includes finance research, forecasting, training, and database-writing capabilities beyond the narrow tracker description. <br>
Mitigation: Review and deploy it as a full finance research toolkit, or remove forecasting, training, report-generation, and write-side tools when only thesis-update tracking is needed. <br>
Risk: The skill may use external market, news, and LLM calls and can produce speculative finance outputs. <br>
Mitigation: Run it only in approved environments, require fresh source-backed evidence, and review outputs before using them for investment decisions. <br>
Risk: Missing or conflicting fresh data can make signal evolution uncertain. <br>
Mitigation: Keep the signal unchanged when evidence is insufficient, mark mixed impact when logic nodes conflict, and state unresolved uncertainties. <br>


## Reference(s): <br>
- [AlphaEar Signal Tracker Prompts](references/PROMPTS.md) <br>
- [ClawHub skill page](https://clawhub.ai/zoeluli7459-dev/skills/alphaear-signal-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Structured JSON or compact human-readable signal update] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Starts with an evolution label and reason, groups evidence by news/event, price/data, and logic-chain impact, and states unresolved uncertainties.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
