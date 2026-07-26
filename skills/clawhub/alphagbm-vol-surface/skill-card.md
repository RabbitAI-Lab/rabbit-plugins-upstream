## Description: <br>
3D volatility surface analysis mapping implied volatility across strikes and expirations, returning surface grid data, ATM term structure, skew by expiry, surface shape, and anomalies for optionable tickers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, traders, and agents use this skill to inspect implied-volatility surfaces for optionable tickers, compare term structure and skew, and flag possible volatility anomalies before further analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker requests and the configured AlphaGBM API key may be sent to AlphaGBM's external service. <br>
Mitigation: Configure the API key only in trusted environments and avoid submitting sensitive or restricted tickers unless external service use is acceptable. <br>
Risk: Volatility surface outputs can be incomplete, stale, or unsuitable as the sole basis for trading decisions. <br>
Mitigation: Independently verify financial outputs and use qualified review before making trading decisions. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API Base URL](https://alphagbm.zeabur.app) <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-vol-surface) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with JSON examples and API endpoint guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include volatility surface grids, ATM term structure, skew by expiry, surface shape classifications, and anomaly flags.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
