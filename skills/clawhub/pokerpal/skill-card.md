## Description: <br>
Query PokerPal poker game data, including games, players, buy-ins, and settlements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vvardhan14](https://clawhub.ai/user/vvardhan14) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Poker group hosts and players use this skill to ask an agent for live PokerPal group, game, player, buy-in, chip count, and net-result information available to the configured bot key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive poker group, player, buy-in, chip count, and net-result data available to the configured bot key. <br>
Mitigation: Install only with a trusted PokerPal API URL, use a least-privilege read-only bot key, and avoid granting access to groups or players whose gambling data should not be visible to the agent. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown] <br>
**Output Format:** [Markdown-style text summaries of PokerPal API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POKERPAL_API_URL and POKERPAL_BOT_API_KEY; responses may include poker buy-in, chip count, and net-result data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
