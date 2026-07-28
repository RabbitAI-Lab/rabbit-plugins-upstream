## Description: <br>
Continuity, durable memory, mood/state, journal, identity diff, heartbeat state, and profile promotion for Valentina/OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to maintain Notion-backed long-term memory, state snapshots, journal synthesis, continuity checks, and profile promotion across agent sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist sensitive mood, journal, identity, and profile data in Notion and local workspace files. <br>
Mitigation: Use it only when durable memory is intended, review Notion workspace permissions, avoid secrets or highly sensitive personal data, and periodically inspect or delete USER.md, memory files, and related Notion databases. <br>
Risk: A custom NOTIONCTL_PATH changes which local Notion helper script the skill runs. <br>
Mitigation: Set NOTIONCTL_PATH only to a trusted local notionctl script, or leave it unset so the configured dependency path is used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire) <br>
- [Publisher profile](https://clawhub.ai/user/nextaltair) <br>
- [Notion integrations](https://www.notion.so/my-integrations) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update Notion records and local workspace memory/profile files when configured.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
