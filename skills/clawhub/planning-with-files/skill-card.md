## Description:

Helps agents manage multi-step work with persistent project planning files and optional lifecycle context reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to track plans, findings, and progress across multi-step projects, with optional reminders from the selected project plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning files may expose sensitive project information when added to agent context.

Mitigation: Keep secrets out of planning files and review their contents before enabling context reminders.

Risk: Explicit session replay may reintroduce excerpts from same-project conversations.

Mitigation: Use replay only when those excerpts are intentionally needed; use metadata mode for aggregate counts.

## Reference(s):

- [Planning with files on ClawHub](https://clawhub.ai/othmanadi/skills/planning-with-files)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown planning files and text guidance with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains task_plan.md, findings.md, and progress.md in the selected project plan directory.]

## Skill Version(s):

3.23.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
