## Description:

当用户需要推翻或修改一个已推进到需求、设计、任务、实现或验证阶段的功能决定时，先只读评估影响，确认后再逐层追平权威产物，并提供可验证、可恢复的执行边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[songzhuozhu](https://clawhub.ai/user/songzhuozhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this skill when a previously approved feature decision must be revised across requirements, design, tasks, implementation, or validation artifacts. It first produces a read-only impact assessment, then updates only the user-confirmed stages and writable roots with recovery logging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete files in user-authorized writable roots after assessment.

Mitigation: Require explicit confirmation of the change assertion, target stage, writable roots, deletion list, conflict handling, hooks, side effects, and disclosed risks before any write.

Risk: The local recovery contract may contain original file contents, including sensitive data, when embedded recovery is used.

Mitigation: Keep the contract at mode 0600, do not stage or commit it, require per-file confirmation for sensitive or large payloads, and delete the contract only after completion or verified restore.

Risk: A partial retcon can leave stale requirements, design, task, implementation, or validation artifacts active.

Mitigation: Use staged gates, dependency tracing, validation baselines, and residual signature scans; block completion when failures or old behavior cannot be explained.

## Reference(s):

- [Read-only Assessment and Execution Confirmation](artifact/references/assessment.md)
- [Reconciliation Contract and Recovery Protocol](artifact/references/contract-schema.md)
- [Semantic Stages and Completion Gates](artifact/references/stage-gates.md)
- [Task Rebuild Rules](artifact/references/task-rebuild.md)
- [Workflow Adapter and Multi-root Execution](artifact/references/spec-kit-adapter.md)
- [Synthetic Case Catalog](artifact/references/case-catalog.md)
- [ClawHub Skill Page](https://clawhub.ai/songzhuozhu/skills/feature-retcon)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, file updates, and JSON status from the recovery script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local 0600 reconciliation contract during confirmed execution; outputs should report modified and deleted file counts, validation results, residual-scan status, stage waterline, and work-root status.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
