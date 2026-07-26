## Description: <br>
Provides a per-ticker 0-100 market fear score that combines VIX, IV Rank, RSI-14, volume anomaly, put/call ratio, and consecutive down days to indicate when a Bull Put Spread entry threshold is met. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and options researchers use this skill to request a ticker-level market fear score and component breakdown as one input for options sentiment and Bull Put Spread timing research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the score or Bull Put Spread signal as personalized financial advice. <br>
Mitigation: Present the score as informational research input and avoid placing options trades solely because the skill reports a signal. <br>
Risk: Options strategies can lose substantial money even when a fear-score signal is present. <br>
Mitigation: Review the component breakdown, confidence, fallback indicators, and independent risk controls before acting on any options strategy. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-fear-score) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Ticker symbol input; score output includes threshold, confidence, and component fallback indicators.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
