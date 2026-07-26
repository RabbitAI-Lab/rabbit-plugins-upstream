## Description: <br>
Check stock prices using the yfinance library without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rupprath](https://clawhub.ai/user/rupprath) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to look up current public stock and ETF market data from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to Yahoo Finance through yfinance when it runs. <br>
Mitigation: Use it only in environments where outbound financial-data requests are allowed. <br>
Risk: Market data fields may be delayed, unavailable, or missing for some symbols. <br>
Mitigation: Treat the output as informational and verify important financial decisions with authoritative sources. <br>


## Reference(s): <br>
- [Yahoo Finance](https://finance.yahoo.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands] <br>
**Output Format:** [Plain text stock quote summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and yfinance; contacts Yahoo Finance/yfinance services at runtime.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
