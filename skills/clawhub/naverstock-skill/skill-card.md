## Description: <br>
Fetch text-based real-time stock prices for KRX and overseas markets using Naver Finance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seungdols](https://clawhub.ai/user/seungdols) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and end users use this skill to run a Node.js command that looks up Korean, overseas, and exchange-rate quote data from Naver Finance and returns a compact JSON result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock, ticker, or currency lookup terms are sent to Naver Finance. <br>
Mitigation: Use only lookup terms you are comfortable sharing with Naver; the skill does not require trading credentials or account access. <br>
Risk: Quote data may be unavailable, stale, or differ between regular KRX and NXT extended-hours markets. <br>
Mitigation: Treat returned prices as informational and verify important values with an authoritative market source before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seungdols/skills/naverstock-skill) <br>
- [Naver Finance](https://finance.naver.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands] <br>
**Output Format:** [JSON emitted by a Node.js command-line script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns quote fields such as name, code, price, change, changePercent, NXT extended-hours values when available, and currency.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
