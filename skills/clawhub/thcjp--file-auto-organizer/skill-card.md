## Description:

File Auto Organizer helps agents organize folders by file type or date, apply custom rules, optionally remove duplicates, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to organize local folders, especially downloads or desktop folders, by file type, date, and custom rules. It is intended for file-management workflows where proposed moves, duplicate deletion, and reports should be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags underspecified file-organizer instructions and destructive duplicate deletion behavior.

Mitigation: Review before installing, use only on non-critical folders or backups, and require a preview before any moves or deletions.

Risk: The security summary flags unrelated API/network guidance that could lead to unnecessary credential handling.

Mitigation: Do not provide API keys unless the publisher documents a specific required service and data flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-auto-organizer)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce file-operation plans, command examples, configuration guidance, and organization reports; preview and backup are recommended before moves or deletions.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
