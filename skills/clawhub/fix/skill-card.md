## Description:

Helps agents analyze behavior-correction feedback, improve the relevant rules or prompts, and finish the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill to investigate an agent's recurring mistakes, improve its behavior instructions, and resume the original task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad correction phrases can trigger changes to persistent agent rules, hooks, or settings.

Mitigation: Invoke explicitly with /fix or fix: and review proposed changes before allowing them.

Risk: Global behavior changes can affect unrelated projects or future sessions.

Mitigation: Prefer --local for project-scoped corrections; review edits to global rules, settings, hooks, and memory files.

## Reference(s):

- [Fix on ClawHub](https://clawhub.ai/drumrobot/skills/fix)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown explanations and plans; edits to agent instructions, configuration, or hooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify persistent project or global agent behavior files and resume the original task.]

## Skill Version(s):

0.8.0 (source: ClawHub release; bundled frontmatter says 0.1.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
