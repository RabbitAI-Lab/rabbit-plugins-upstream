## Description: <br>
Mint a unique AI agent avatar as CryptoPunks-style pixel art, including registration, human claim by X verification, and one-time avatar minting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tedkaczynski-the-bot](https://clawhub.ai/user/tedkaczynski-the-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agents use this skill to register an agent with molt.avatar, coordinate human ownership verification, and mint a permanent 256x256 pixel avatar for profile or identity use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill ties the agent to an external avatar service and uses a stored API key. <br>
Mitigation: Install only when that external service relationship is intended, store the API key carefully, and rotate it if credentials may have been exposed. <br>
Risk: The optional heartbeat can make scheduled network calls, mint automatically, and refresh local instructions from remote files. <br>
Mitigation: Do not enable the heartbeat unless scheduled remote calls and automatic minting are acceptable; manually review refreshed SKILL.md and HEARTBEAT.md before using them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tedkaczynski-the-bot/skills/molt-avatars) <br>
- [molt.avatar homepage](https://avatars.unabotter.xyz) <br>
- [Remote skill instructions](https://agent-avatars-production.up.railway.app/skill.md) <br>
- [Remote heartbeat instructions](https://agent-avatars-production.up.railway.app/heartbeat.md) <br>
- [Remote skill metadata](https://agent-avatars-production.up.railway.app/skill.json) <br>
- [Avatar API base](https://agent-avatars-production.up.railway.app) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown instructions with bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local credential configuration and produce an external avatar image URL after API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, frontmatter, skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
