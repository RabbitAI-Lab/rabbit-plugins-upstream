## Description:

Reconstructs project timelines, tracks problems and solutions, extracts reusable lessons from AI-assisted projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to review complex AI-assisted projects, reconstruct what happened across sessions, and turn problems, decisions, and lessons into a reusable retrospective document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to read local project memory and session-history files while reconstructing past work.

Mitigation: Use it only for an intended project directory and require confirmation before reading outside the workspace.

Risk: The skill may result in writes to memory or documentation files after a retrospective.

Mitigation: Review proposed updates before allowing the agent to modify memory, documentation, or checklist files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiyan521/skills/project-retrospective)
- [Publisher profile](https://clawhub.ai/user/shiyan521)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown retrospective document with structured timelines, problem summaries, decisions, and lessons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also propose updates to project memory, reusable skills, or project checklists after the retrospective.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
