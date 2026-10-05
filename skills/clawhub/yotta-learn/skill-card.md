## Description:

Captures agent mistakes, corrections, and insights as reusable lessons and stores reviewed knowledge in a searchable knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users capture lessons after failures or corrections, resolve recurring issues, and review verified knowledge across sessions and agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persisted lessons or knowledge entries may expose secrets, sensitive paths, or full logs to later sessions.

Mitigation: Record only concise, redacted lessons; do not store tokens, private keys, full logs, or sensitive paths in .learnings/ or the knowledge base.

Risk: Optional hooks may trigger review reminders on every prompt or command failure.

Mitigation: Keep hooks disabled unless those reminders are wanted; enable and review hook configuration deliberately.

Risk: Unpinned installation may select a different release than the one reviewed.

Mitigation: Use a pinned install command for the reviewed release.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage (listed in ClawHub metadata)](https://github.com/YottaMeta/yotta-learn)
- [Knowledge base reference](references/kb.md)
- [Hook setup reference](references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown lesson and knowledge entries with plain-text CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lessons and knowledge-base entries persist locally for reuse across sessions.]

## Skill Version(s):

0.3.0 (source: ClawHub release, SKILL.md frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
