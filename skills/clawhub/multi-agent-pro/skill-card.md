## Description:

Multi Agent Orchestrator helps agents define, validate, execute, resume, report on, and visualize DAG-based multi-agent pipelines with shared state, approvals, retries, templates, and recovery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to turn multi-step work such as collection, analysis, review, and reporting into DAG-based agent workflows with shared state, checkpoint recovery, and execution reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs local workflow orchestration and can create or modify pipeline state, report, history, and snapshot files.

Mitigation: Install it only for local workflow orchestration use cases and keep state and output paths inside a dedicated workspace.

Risk: Node outputs, error messages, reports, and state files may contain sensitive data because the skill does not automatically redact user-provided content.

Mitigation: Do not store secrets or raw credentials in node outputs or errors, and redact sensitive fields before completing or failing workflow nodes.

Risk: Untrusted templates or dependency names can broaden file handoffs, approvals, video-analysis steps, or external-service use.

Mitigation: Review pipeline templates and dependency names before running them, especially when they involve approvals, video analysis, external services, or broad file exchange.

Risk: Multiple orchestration runs writing to the same state file can corrupt or confuse workflow status.

Mitigation: Use a separate state file path for each pipeline run and avoid sharing the same state file across concurrent orchestrator instances.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/multi-agent-pro)
- [DAG Scheduling Guide](artifact/references/dag-scheduling-guide.md)
- [State Sharing Protocol](artifact/references/state-sharing-protocol.md)
- [Error Recovery Patterns](artifact/references/error-recovery-patterns.md)
- [Complete Usage Examples](artifact/references/examples.md)
- [Anti-Patterns](artifact/references/anti-patterns.md)
- [Deep FAQ](artifact/references/faq-deep.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON pipeline definitions, Python shell commands, and generated Markdown or HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local workflow outputs can include pipeline state, execution history, snapshots, Markdown reports, and HTML Gantt charts.]

## Skill Version(s):

5.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
