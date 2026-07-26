## Description: <br>
Analyzes a single options expiration's implied volatility smile and skew, returning smile curve data, 25-delta skew, risk reversal, shape classification, skew percentile, and trading interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and trading analysts use this skill to examine options volatility smile shape, put/call skew, and skew metrics for a ticker and expiration. The results help frame market-implied tail risk and skew trade ideas as informational analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker and expiry queries are sent to the external AlphaGBM service, and use may require storing an ALPHAGBM_API_KEY in the agent environment. <br>
Mitigation: Confirm that sending those queries to AlphaGBM is acceptable for the deployment and store the API key only in the agent environment or an approved secret store. <br>
Risk: Options volatility and skew analysis could be mistaken for financial advice. <br>
Mitigation: Treat the output as informational market analysis and require human review before making trading or risk decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-vol-smile) <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with volatility smile metrics, JSON-shaped response examples, and API request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes ticker and expiration inputs, implied volatility curve data, skew metrics, shape classification, skew percentile, and informational interpretation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
