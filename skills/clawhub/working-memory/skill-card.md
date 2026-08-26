## Description:

Maintain a project's mid-term working memory in a WORKING.md file that captures the current stage, decisions, failed attempts, and next steps so work can resume after context compaction or a new session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ikotelkin](https://clawhub.ai/user/ikotelkin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to preserve project state across long coding sessions, compaction, and handoffs. It helps an agent create, read, checkpoint, and consolidate a local WORKING.md file containing stage context, decisions, dead ends, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WORKING.md can capture sensitive project details if checkpointed without review.

Mitigation: Review WORKING.md before checkpointing sensitive work and keep entries limited to the operational state needed for resuming.

Risk: Generic trigger words such as "checkpoint" can cause unintended updates to local memory files.

Mitigation: Use explicit prompts when saving state and confirm the intended WORKING.md location before writing.

## Reference(s):

- [Working Memory ClawHub release](https://clawhub.ai/ikotelkin/skills/working-memory)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

## Skill Output:

**Output Type(s):** [Markdown, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown files and concise agent instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or updates local project memory files such as WORKING.md and optional CLAUDE.md pointers.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
