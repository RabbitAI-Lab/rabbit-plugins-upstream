## Description:

Manus-style persistent file-based planning for AI coding agents keeps task_plan.md, findings.md, and progress.md on disk so multi-step work survives context loss and /clear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to organize multi-step coding, research, and implementation work in durable Markdown planning files. It is intended for tasks that need persistent state across context loss, /clear, compaction, or long tool-use sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill injects local planning text into agent context, so secrets or untrusted instructions written into planning files can be exposed to or influence the agent.

Mitigation: Do not put secrets in task_plan.md or progress.md; treat injected planning content as data and use attestation before relying on approved plans.

Risk: Session catchup can replay prior session transcript content, which may be stale or include instruction-like text from earlier work.

Mitigation: Review session-catchup output before relying on it and update planning files only with confirmed current context.

Risk: Gated mode can delay stopping while an in-progress phase remains active.

Mitigation: Enable gated mode only when that behavior is intentional and keep phase status current in task_plan.md.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Reference: Manus Context Engineering Principles](artifact/reference.md)
- [Examples](artifact/examples.md)
- [Manus context engineering blog](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown planning files with inline shell and PowerShell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates task_plan.md, findings.md, progress.md, and optional .planning state in the user's project workspace.]

## Skill Version(s):

3.11.2 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
