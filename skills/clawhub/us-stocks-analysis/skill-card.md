## Description: <br>
US Stocks Analysis guides agents through read-only U.S. equity research using SentiSense data, public SEC/FRED sources, quick data workflows, and an adversarial investment committee that records sourced bull, bear, and dissenting views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask agents for sourced U.S. stock research, fast market-data briefs, due diligence, and thesis review. It is intended for educational analysis and explicitly avoids trading, purchases, wallet access, and write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock analysis output may be mistaken for personalized investment advice. <br>
Mitigation: Keep the skill's educational-use framing, no-advice disclaimer, and user decision responsibility visible in outputs. <br>
Risk: Research quality depends on the freshness and availability of SentiSense, SEC, and FRED data. <br>
Mitigation: Require sourced evidence rows, as-of dates, and explicit unavailable markers instead of guesses. <br>
Risk: API use requires sharing a SentiSense API key with the agent runtime. <br>
Mitigation: Install only in environments where the user accepts that credential use and can manage the key securely. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis) <br>
- [SentiSense website](https://sentisense.ai) <br>
- [SentiSense API reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key) <br>
- [SEC company tickers reference](https://www.sec.gov/files/company_tickers.json) <br>
- [SEC XBRL company concept API](https://data.sec.gov/api/xbrl/companyconcept/CIK{10digits}/us-gaap/{Concept}.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown narrative with sourced tables, checklist-style verdicts, and occasional inline API call examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only informational output; not personalized investment advice or trading instructions.] <br>

## Skill Version(s): <br>
2.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
