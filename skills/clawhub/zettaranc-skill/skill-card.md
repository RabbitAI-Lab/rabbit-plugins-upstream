## Description: <br>
Zettaranc Perspective helps agents provide Chinese-language educational decision support for A-share stock analysis, portfolio review, trade recap, and career or business questions using the Zettaranc framework. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lululu811](https://clawhub.ai/user/lululu811) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill for Chinese-language A-share technical analysis, stock-framework explanations, portfolio or trade-record review, and Zettaranc-style career, life, or business decision framing. It is educational decision support and is not a trading execution system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for a market-data API token. <br>
Mitigation: Use a contained workspace and avoid pasting secrets into chat unless the runtime is trusted. <br>
Risk: The skill may read or write local configuration and persist reports, trade records, or investment preferences. <br>
Mitigation: Review the workspace contents and persistence behavior before installation and use. <br>
Risk: Trading-related output could be mistaken for instructions to trade. <br>
Mitigation: Treat all trading output as educational decision support and keep human review over all investment decisions. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/lululu811/zettaranc-skill) <br>
- [ClawHub skill page](https://clawhub.ai/lululu811/skills/zettaranc-skill) <br>
- [Workflow reference](artifact/knowledge/workflow.md) <br>
- [Harness and guardrails reference](artifact/knowledge/harness.md) <br>
- [Improvement system reference](artifact/knowledge/improvement-system.md) <br>
- [Tushare token page](https://tushare.pro/user/token) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown responses with optional command suggestions, configuration steps, and local report files when supported by the runtime.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask for a Tushare market-data token, read or write local configuration, save reports and trade records, and remember investment preferences.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
