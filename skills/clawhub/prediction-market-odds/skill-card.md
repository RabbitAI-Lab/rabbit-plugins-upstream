## Description: <br>
Gets live prediction-market odds and implied probabilities for future-event forecasting, betting, hedging, and market-calibration workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rccola990-cloud](https://clawhub.ai/user/rccola990-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve market-implied odds before forecasting, betting, hedging, or comparing an internal estimate against active prediction markets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends forecasting queries to store.agentexchange.work. <br>
Mitigation: Use it only when sharing the query topic with that endpoint is acceptable. <br>
Risk: Using the endpoint can authorize small USDC x402 payments. <br>
Mitigation: Review the HTTP 402 price before payment and only approve calls you intend to make. <br>
Risk: Prediction-market odds can be mistaken for financial or betting advice. <br>
Mitigation: Treat returned market odds as advisory data and apply separate judgment before forecasting, betting, or hedging. <br>


## Reference(s): <br>
- [Prediction market odds endpoint](https://store.agentexchange.work/markets/prediction?q=<TOPIC or QUESTION>) <br>
- [Agent Exchange sample catalog](https://store.agentexchange.work/samples) <br>
- [ClawHub skill page](https://clawhub.ai/rccola990-cloud/skills/prediction-market-odds) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with an HTTP GET example and endpoint guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The external endpoint returns matching markets with current prices, implied probability, and venue.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
