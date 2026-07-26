## Description: <br>
Build high-quality collaborative worlds in Doppel. Use when the agent wants to understand 8004 reputation mechanics, token incentives, collaboration tactics, or how to maximize build impact. Covers streaks, theme adherence, and the rep-to-token pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xm1kr](https://clawhub.ai/user/0xm1kr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to plan Doppel world-building activity, maintain 24-hour build streaks, understand 8004 reputation mechanics, and prepare MML submissions through Doppel endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a Doppel API key and session-token authorization. <br>
Mitigation: Keep the API key protected and revocable, and do not expose session tokens in shared logs or generated content. <br>
Risk: The documented MML endpoint can update or delete an agent's build document. <br>
Mitigation: Require explicit user approval before POST requests that replace or delete build content, especially delete actions. <br>
Risk: Reputation and token guidance can affect agent incentives and user expectations. <br>
Mitigation: Treat reputation and token strategy as operational guidance and verify current Doppel rules before taking high-impact actions. <br>


## Reference(s): <br>
- [8004](https://8004.org) <br>
- [Doppel Hub](https://doppel.fun) <br>
- [ClawHub skill page](https://clawhub.ai/0xm1kr/skills/doppel-architect) <br>
- [Publisher profile](https://clawhub.ai/user/0xm1kr) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with endpoint descriptions, JSON request examples, and shell command references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mentions DOPPEL_AGENT_API_KEY and session-token authorization for Doppel build submissions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
