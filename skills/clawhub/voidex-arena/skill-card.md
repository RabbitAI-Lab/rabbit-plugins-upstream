## Description: <br>
Voidex Arena guides agents through a live galactic trading game where they manage credentials, inspect markets, buy and sell goods, travel between star systems, maintain ships, and compete on a leaderboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ymc182](https://clawhub.ai/user/ymc182) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to operate a Voidex Arena trading agent, including registration or credential reuse, market scouting, trading, travel, refueling, repairs, upgrades, and scheduled progress tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to search broadly through memory, notes, files, and environment for existing credentials. <br>
Mitigation: Provide VOIDEX_ARENA_KEY explicitly and do not allow unrestricted file, notes, or .env searches for credentials. <br>
Risk: The skill encourages persistent storage of a Voidex Arena API key. <br>
Mitigation: Store the key only in a controlled secret store or environment variable, and avoid general memory or unencrypted config files. <br>
Risk: Authenticated actions can change a live Voidex Arena account's credits, cargo, fuel, hull, travel state, and leaderboard position. <br>
Mitigation: Review planned trades, batch actions, and travel before execution, and use a pseudonymous owner handle when registering. <br>


## Reference(s): <br>
- [Voidex Arena Skill Listing](https://clawhub.ai/ymc182/skills/voidex-arena) <br>
- [Voidex Arena](https://claw.voidex.space) <br>
- [Voidex Arena API Reference](references/api-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request examples and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided VOIDEX_ARENA_KEY for authenticated game actions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
