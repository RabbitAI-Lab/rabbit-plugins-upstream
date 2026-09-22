## Description:

Planning with Files helps agents maintain persistent project plans, findings, and progress logs on disk, with lifecycle hooks that inject selected planning context for multi-step work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep long-running or multi-step work organized through durable markdown planning files, recovery scripts, and lifecycle hook context injection. It is most relevant when a task spans several tool calls, research steps, implementation phases, or collaborating agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lifecycle hooks read and inject project planning files into agent context.

Mitigation: Do not store secrets or sensitive credentials in planning files, and review plan content before enabling workflows that repeatedly inject it.

Risk: Explicit session replay can expose bounded same-project transcript excerpts.

Mitigation: Use metadata mode for aggregate counts by default, and use replay only after explicit approval for the active project.

Risk: Autonomous or gated modes can cause an agent to continue based on the selected plan.

Mitigation: Enable these modes only when continuation is intended, keep the active plan pinned, and re-attest the plan after intentional edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Reference: Manus Context Engineering Principles](reference.md)
- [Examples: Planning with Files in Action](examples.md)
- [Task plan template](templates/task_plan.md)
- [Findings template](templates/findings.md)
- [Progress template](templates/progress.md)
- [Manus context engineering article](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Attestation locking and fallback](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/attestation-locking.md)
- [Performance notes](https://github.com/OthmanAdi/planning-with-files/blob/master/docs/perf-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions, planning-file templates, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and updates project-local planning files such as task_plan.md, findings.md, and progress.md; lifecycle hooks may inject selected planning context into agent turns.]

## Skill Version(s):

3.20.5 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
