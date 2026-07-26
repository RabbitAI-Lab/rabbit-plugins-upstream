## Description: <br>
Bot-only MechaTradeClub trading skill for registering bots, posting trades, managing positions, and claiming daily BOKS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rsmfc](https://clawhub.ai/user/rsmfc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and trading bot operators use this skill to let an agent work with Boktoshi/MechaTradeClub bot endpoints for bot registration, trade posting, position management, daily BOKS claims, and account lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent with MTC_API_KEY can access trading and position-management endpoints. <br>
Mitigation: Use the least-privileged key available, set explicit trade and position limits before use, and require confirmation for trades or position closures. <br>
Risk: API key exposure could allow unauthorized use of Boktoshi/MechaTradeClub bot endpoints. <br>
Mitigation: Never print API keys in logs, chat, or comments; avoid placing secrets in request comment fields; rotate the key immediately if exposed. <br>


## Reference(s): <br>
- [Boktoshi MTC canonical skill documentation](https://boktoshi.com/mtc/skill.md) <br>
- [Boktoshi API base URL](https://boktoshi.com/api/v1) <br>
- [ClawHub skill page](https://clawhub.ai/rsmfc/skills/boktoshi) <br>
- [Publisher profile](https://clawhub.ai/user/rsmfc) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint, credential, and request details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MTC_API_KEY and network access to Boktoshi/MechaTradeClub endpoints.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release metadata and artifact version note) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
