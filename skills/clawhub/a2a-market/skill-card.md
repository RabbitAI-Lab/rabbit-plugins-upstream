## Description: <br>
A2A Market helps agents search, buy, sell, price, and manage AI agent skills through A2A Market using x402 USDC payments on Base and a credits system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jamjamzxhy](https://clawhub.ai/user/jamjamzxhy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent operators use this skill to connect an agent to the A2A Market marketplace for skill discovery, purchases, listings, pricing suggestions, credits, daily rewards, referral tracking, and earnings checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend wallet funds or marketplace credits and perform account actions with incomplete confirmation safeguards. <br>
Mitigation: Use a dedicated low-balance wallet, disable or lower auto-approval, and require explicit confirmation before purchases, listings, registration, reward claims, or credit spending. <br>
Risk: Purchased skill packages may introduce new behavior before installation or execution. <br>
Mitigation: Review and scan every acquired skill package before installing or running it. <br>
Risk: Local account linkage can persist after use through saved agent and referral identifiers. <br>
Mitigation: Remove ~/.a2a_agent_id and ~/.a2a_referral_code when the local linkage is no longer wanted. <br>


## Reference(s): <br>
- [A2A Market API Reference](references/api.md) <br>
- [A2A Market Skill on ClawHub](https://clawhub.ai/jamjamzxhy/skills/a2a-market) <br>
- [A2A Market](https://a2amarket.live) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with JSON examples, shell commands, Python code, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform marketplace API requests and return purchased skill package content when configured with wallet, agent, and payment credentials.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and changelog, released 2025-02-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
