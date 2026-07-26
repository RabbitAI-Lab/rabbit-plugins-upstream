## Description: <br>
Helps agents manage A-share watchlists, monitor market conditions, draft trading plans, track positions, and set price alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cooperiano](https://clawhub.ai/user/cooperiano) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to maintain A-share watchlists, record transactions, prepare monitoring routines, and structure trading-plan guidance. Outputs should be treated as planning support, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Watchlists, transaction notes, and alerts may be stored as plaintext under ~/.openclaw/a_share. <br>
Mitigation: Do not store broker credentials, account secrets, or sensitive personal financial data in those files, and remove the directory when the skill is no longer used. <br>
Risk: Trading-plan outputs may be incomplete or misleading if market data is stale, missing source labels, or interpreted as investment advice. <br>
Mitigation: Confirm data source and timestamp, avoid absolute claims, and require human review before making trading decisions. <br>


## Reference(s): <br>
- [A Share Trading on ClawHub](https://clawhub.ai/cooperiano/skills/a-share-trading) <br>
- [Publisher profile: cooperiano](https://clawhub.ai/user/cooperiano) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with plain-text file schemas, trading-plan templates, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local plaintext files under ~/.openclaw/a_share for watchlists, transactions, and alerts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
