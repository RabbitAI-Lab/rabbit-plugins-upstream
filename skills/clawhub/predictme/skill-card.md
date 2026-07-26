## Description: <br>
Trade 10-second crypto prediction markets on PredictMe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[howardpen9](https://clawhub.ai/user/howardpen9) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and AI-agent operators use this skill to register a PredictMe agent, configure trading preferences, retrieve market odds, and place TEST or BONUS balance bets on short crypto prediction rounds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place autonomous crypto prediction-market bets using TEST or BONUS balances. <br>
Mitigation: Require explicit owner approval until the strategy is proven, set per-bet and session spend limits, enforce stop-losses and trading hours, and pause after weak performance. <br>
Risk: The skill stores a PredictMe API key and agent ID for future authenticated requests. <br>
Mitigation: Store credentials in a secrets manager or locked-down user file outside project directories, add any local credential file to .gitignore, and rotate credentials if exposed. <br>
Risk: Trading guidance can lead to overconfident or misleading decisions in a fast prediction market. <br>
Mitigation: Observe and paper trade before placing bets, log each decision, review bet history regularly, and avoid scaling until measured performance supports it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/howardpen9/skills/predictme) <br>
- [PredictMe Agent Trading Guide](https://app.predictme.me/skill.md) <br>
- [PredictMe Agent API Spec](https://app.predictme.me/agents.json) <br>
- [PredictMe Agent Discovery](https://app.predictme.me/agent-card.json) <br>
- [PredictMe Agents Page](https://app.predictme.me/agents) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown with JSON and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes registration, credential storage, owner preference, betting-loop, bankroll, nonce, and commentary guidance.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
