## Description:

multi-agent-pro helps agents define, validate, execute, resume, report on, and visualize multi-agent DAG pipelines with shared local state, approval nodes, nested pipelines, snapshots, and update checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to break complex tasks into local multi-agent DAG pipelines, coordinate execution and recovery, and generate execution reports or visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow state, history, reports, snapshots, child state, and recovery checkpoints can retain node outputs locally.

Mitigation: Avoid storing secrets, credentials, or private data in node outputs; review retained local artifacts before sharing or archiving them.

Risk: Generated pipeline paths may write state, reports, snapshots, or registry data in unintended locations.

Mitigation: Install only in trusted workspaces and review generated pipeline paths before running the scripts.

Risk: Generated HTML can be unsafe when pipeline names or node names come from untrusted sources.

Mitigation: Treat generated HTML reports and Gantt charts as untrusted content unless all displayed pipeline and node names are trusted.

Risk: The update check may make outbound network requests.

Mitigation: Run the update check only when outbound network access is acceptable for the workspace.

## Reference(s):

- [DAG Scheduling Guide](references/dag-scheduling-guide.md)
- [State Sharing Protocol](references/state-sharing-protocol.md)
- [Error Recovery Patterns](references/error-recovery-patterns.md)
- [Usage Examples](references/examples.md)
- [Deep FAQ](references/faq-deep.md)
- [Anti-Patterns](references/anti-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON state, Markdown reports, HTML Gantt charts, snapshots, and registry files when the bundled scripts are run.]

## Skill Version(s):

5.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
