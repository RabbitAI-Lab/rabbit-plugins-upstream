## Description: <br>
Polymarket Edge Detector scans binary prediction markets for apparent pricing edges by comparing market prices with reference probabilities and ranking opportunities by edge, liquidity, time to resolution, and confidence. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Prediction market traders, sports bettors, and DeFi quants can use this skill to prototype screening workflows for Polymarket-style binary contracts. The bundled implementation is suitable for demonstration because the security evidence identifies its data source as mock/random rather than reliable market and reference-data integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake BUY_YES or BUY_NO outputs for reliable real-money trading signals even though the implementation uses mock random data. <br>
Mitigation: Treat outputs as demonstration data only until the publisher replaces the mock generator with real Polymarket and reference-data integrations and labels synthetic mode clearly. <br>
Risk: Skill text describes production Polymarket analysis more strongly than the current artifact behavior supports. <br>
Mitigation: Review the artifact before deployment and confirm whether it is operating in mock or production-data mode before acting on any signal. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/polymarket-edge-detector) <br>
- [Polymarket CLOB API endpoint](https://clob.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces market screening records with fields such as market_id, question, category, prices, reference probability, edge, liquidity, days to resolution, signal, and confidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
