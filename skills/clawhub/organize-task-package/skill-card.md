## Description:

Organizes complex development, repair, testing, research, migration, or operational work into executable, resumable, independently reviewable task documentation packages with launch configuration guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukp20](https://clawhub.ai/user/xukp20)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical project leads use this skill to turn complex or evolving work into durable task packages with design decisions, GOAL state, execution receipts, review records, and launch settings for Workers and Reviewers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide Codex to read repository state and create task-package files.

Mitigation: Install it only in workspaces where that behavior is intended, require user authorization before writing, and review generated package diffs.

Risk: Launch configuration may include Worker or Reviewer sessions, worktrees, external runs, migrations, pushes, or cleanup actions.

Mitigation: Review and confirm the proposed launch configuration before allowing those actions.

Risk: Incorrect task records can preserve mistaken requirements or misleading completion status.

Mitigation: Use the skill's discussion recovery, design gates, execution receipts, and review records before marking work approved.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/xukp20/skills/organize-task-package)
- [Server-resolved GitHub source](https://github.com/xukp20/codex-task-package/tree/main/skills/organize-task-package)
- [Discussion Recovery and Task Design](references/design-and-planning.md)
- [Task Package Structure and Initialization](references/package-structure.md)
- [Launch Configuration Recommendation and Confirmation](references/launch-configuration.md)
- [Worker and Reviewer Session Topology](references/session-topology.md)
- [Worker Execution and Review](references/execution-and-review.md)
- [Parallel Worker Orchestration](references/parallel-orchestration.md)
- [Task-Type Profiles](references/task-profiles.md)
- [Lessons from Existing Task Records](references/observed-lessons.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown task documents, launch summaries, scaffolded files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create task package files after user authorization; the bundled initializer refuses to overwrite existing directories.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
