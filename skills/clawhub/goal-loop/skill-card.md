## Description:

Goal Loop supervises complex multi-step agent work by maintaining an explicit goal ledger, requiring evidence-backed validation, supporting checkpointed resumption, and blocking premature completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bz-ai](https://clawhub.ai/user/bz-ai)

### License/Terms of Use:

Proprietary

## Use Case:

Developers, operators, and agent users apply this skill to keep complex software, document, data, research, and multi-agent tasks complete, verified, and resumable. It is intended for work where skipped requirements, unverified results, or early stopping would be costly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update PROJECT-CHECKPOINT.md, leaving persistent task state in the project root.

Mitigation: Use it only in projects where a persistent checkpoint file is acceptable, and review the checkpoint before sharing or publishing repository contents.

Risk: The workflow requires reading project context to maintain a ledger and resume work.

Mitigation: Avoid installing or invoking it in sensitive repositories unless the agent's access to project files is appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bz-ai/skills/goal-loop)
- [README](artifact/README.md)
- [Project checkpoint template](artifact/templates/PROJECT-CHECKPOINT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured ledgers, checkpoint files, validation notes, and task-specific code or command suggestions when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update PROJECT-CHECKPOINT.md for long-running or complex projects.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
