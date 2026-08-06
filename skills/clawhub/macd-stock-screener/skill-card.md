## Description: <br>
A Chinese-language A-share MACD stock screener that finds right-side golden-cross and left-side approaching-cross candidates, collects East Money forum sentiment, and generates daily CSV and Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunsongyeah](https://clawhub.ai/user/sunsongyeah) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run a Chinese-language A-share MACD screening workflow that identifies right-side golden-cross and left-side approaching-cross candidates and optionally summarizes East Money forum sentiment. It provides screening support only; it does not backtest strategies, place trades, or access brokerage accounts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Screening outputs may be mistaken for investment advice. <br>
Mitigation: Treat generated candidates and reports as screening information and require independent review before any financial decision. <br>
Risk: Full scans and sentiment collection may make many public data requests and encounter captcha or rate controls. <br>
Mitigation: Use scan-only or skip-sentiment modes when appropriate, respect source-site access limits, and stop collection when captcha detection is reported. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunsongyeah/skills/macd-stock-screener) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [macd_screener.py](artifact/scripts/macd_screener.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, CSV files, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated CSV candidate lists and Markdown sentiment and summary reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes reports under outputs/YYYY-MM-DD by default and supports options for output path, candidate count, right-only, left-only, scan-only, and skipped sentiment collection.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
