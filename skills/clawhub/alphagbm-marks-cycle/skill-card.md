## Description: <br>
Provides a Howard Marks-style 0-100 market cycle score by blending VIX, SPY IV Rank, put/call ratio, and valuation percentile into an offense-vs-defense posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent builders use this skill to request a market-level cycle read and receive a cycle score, signal breakdown, and plain-language offensive or defensive posture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may answer broad market questions with action-oriented trading posture. <br>
Mitigation: Treat the output as a rough market sentiment indicator, not personalized financial advice, and independently verify data, suitability, and risk before acting. <br>
Risk: The security review flags limited risk framing for direct trading posture recommendations. <br>
Mitigation: Review the skill before installation and add user-facing risk framing where it will be used in financial workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-marks-cycle) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [JSON with plain-language posture text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Market-level output with no ticker input; endpoint is described as free, unauthenticated, and cached for 5 minutes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
