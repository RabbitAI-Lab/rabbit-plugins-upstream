## Description:

Updates installed SenseNova sn-* skills in OpenClaw or hermes-agent, either across the whole bundle or for specific named skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to refresh installed SenseNova skills in OpenClaw or hermes-agent, with scope control for the whole bundle or named sn-* skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can replace installed sn-* skills.

Mitigation: Review the selected update scope before running and keep separate backups if more rollback history is required.

Risk: Older backup buckets may be pruned after an update run.

Mitigation: Preserve any long-term rollback copies outside the agent backup directory before running updates.

Risk: A user-supplied fork URL can change the source of installed skills.

Mitigation: Prefer the default OpenSenseNova repository unless the fork is explicitly trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-update)
- [SenseNova-Skills repository referenced by the skill](https://github.com/OpenSenseNova/SenseNova-Skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command snippets and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report updated, already up-to-date, backup, and error groups.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
