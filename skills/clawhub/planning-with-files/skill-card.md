## Description:

Persistent file-based planning for multi-step AI-agent work that keeps task_plan.md, findings.md, and progress.md on disk while lifecycle hooks inject selected planning context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to maintain durable task plans, findings, progress logs, and task-specific planning state across complex or long-running AI-agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lifecycle hooks and local planning files can add selected project planning context to agent turns.

Mitigation: Install from ClawHub or a pinned, verified source revision and review planning files and hooks before deployment.

Risk: Explicit session-catchup.py --replay can expose bounded same-project transcript excerpts to the agent context.

Mitigation: Use metadata mode for aggregate counts by default, and use replay only when that exposure is acceptable.

Risk: Optional gated mode can resist stopping while a plan still reports work remaining.

Mitigation: Enable gated mode only for workflows where continued execution is intended, and keep plan phase status current.

Risk: The skill writes planning and ledger state into project directories.

Mitigation: Pin PLAN_ID or PWF_PLAN_ROOT for isolated tasks and inspect generated planning files before sharing or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Examples: Planning with Files in Action](examples.md)
- [Reference: Manus Context Engineering Principles](reference.md)
- [Manus Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Attestation locking documentation](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/attestation-locking.md)
- [Performance notes documentation](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/perf-notes.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown planning files with inline shell commands and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update task_plan.md, findings.md, progress.md, and .planning state in the project workspace.]

## Skill Version(s):

3.16.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
