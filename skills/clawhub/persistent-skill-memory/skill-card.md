## Description:

Stops an agent from forgetting the skills it has installed by generating a categorized capability index from installed SKILL.md frontmatter and injecting it into the durable system prompt between stable markers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep installed skills discoverable across context resets or workspace restoration by maintaining a compact capability index in durable agent memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to persistently modify an agent's durable prompt.

Mitigation: Install only when durable memory changes are intended; require a dry run or clear diff, keep a prompt backup, and review the final prompt before relying on it.

Risk: Auto-refresh hooks can keep changing the skill index after installation, invention, or restore workflows.

Mitigation: Make hooks opt-in, easy to remove, and scoped to the selected workspace; inspect outputs and exit codes after each refresh.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/persistent-skill-memory)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and bounded prompt-index text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local durable prompt markers and a generated skills index when executed.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
