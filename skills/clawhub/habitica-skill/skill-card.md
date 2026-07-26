## Description: <br>
Habitica gamified habit tracker integration for listing, creating, completing, and updating habits, dailies, todos, and rewards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tonyunturn](https://clawhub.ai/user/tonyunturn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to inspect and manage Habitica tasks, character stats, inventory, party chat, class skills, quests, and daily cron actions through a shell-backed CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Habitica API token can read and modify the user's Habitica account. <br>
Mitigation: Install only when comfortable granting that access, keep ~/.habitica private, and avoid committing or sharing the token. <br>
Risk: Commands such as delete, party-send, quest-accept, cast, cron, and bulk scoring can change account or party state. <br>
Mitigation: Require explicit confirmation before running mutating commands and review task IDs, messages, quest actions, and batch operations before execution. <br>


## Reference(s): <br>
- [Habitica API v3](https://habitica.com/api/v3) <br>
- [ClawHub Habitica Skill Page](https://clawhub.ai/tonyunturn/skills/habitica-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Habitica user ID and API token configuration; uses curl and jq; notes a 30 second rate limit between automated calls.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
