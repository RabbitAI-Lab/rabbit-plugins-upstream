## Description: <br>
Quantifies whether a stock is suitable for long-term holding or requires tiered profit-taking using a rollercoaster-rate metric and 15 exit-strategy backtests over about 10 years of daily history per ticker. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and investing-workflow agents use this skill to analyze whether a ticker is better suited to long holding or tiered profit-taking. It returns comparative exit-strategy metrics that can inform sell-plan discussion, review, or configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce concrete stock sell-order guidance without explicit suitability checks or financial-risk framing. <br>
Mitigation: Require human review before acting on outputs and present results as analytical support rather than personalized financial advice. <br>
Risk: The skill uses an external AlphaGBM API that may consume credits for first-time ticker analysis and cache results globally. <br>
Mitigation: Inform users before first-time ticker computation and avoid submitting sensitive portfolio context beyond the ticker needed for analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-take-profit) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API request and response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce concrete sell-order guidance and consume one stock-analysis credit for first-time ticker computation; cached ticker reads are described as faster and no-quota.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
