## Description: <br>
多币种记录旅行消费、汇率自动换算、分类统计与预算管理，帮助旅行者跟踪支出并进行AA分摊。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and trip planners use this skill to record expenses across currencies, review category/date/currency summaries, and check total or daily budgets during travel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel expense details are stored in local JSON files inside the skill directory. <br>
Mitigation: Install only if local storage is acceptable, avoid entering unnecessary sensitive payment details, and manage or delete local expense files according to privacy needs. <br>
Risk: Currency conversion uses built-in reference exchange rates rather than live market rates. <br>
Mitigation: Treat converted totals as estimates and verify current exchange rates before making financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-expense-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Natural-language responses grounded in JSON outputs from the expense tracker script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON expense files and built-in reference exchange rates; no external API key is required.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
