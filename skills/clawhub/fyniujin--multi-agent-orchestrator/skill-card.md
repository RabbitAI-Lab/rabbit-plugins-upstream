## Description:

Multi-Agent Pro helps agents define, validate, execute, resume, and visualize DAG-based multi-agent pipelines with shared local state, approval nodes, recovery flows, snapshots, cost tracking, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to break complex work into DAG-based multi-agent pipelines, manage local execution state, resume failed runs, and produce execution reports or visualizations. It is best suited for local workflow orchestration where the user supplies or approves the pipeline definition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local pipeline state, snapshots, and generated reports can preserve sensitive task outputs.

Mitigation: Keep pipeline and state paths inside a project directory, avoid putting secrets or regulated data in node outputs, and review reports or snapshots before sharing them.

Risk: The bundled financial auto-approval example could be mistaken for a production approval policy.

Mitigation: Treat the financial auto-approval template as a demo and replace it with a reviewed approval process before using it for real decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/multi-agent-orchestrator)
- [DAG scheduling guide](references/dag-scheduling-guide.md)
- [State sharing protocol](references/state-sharing-protocol.md)
- [Error recovery patterns](references/error-recovery-patterns.md)
- [Anti-patterns](references/anti-patterns.md)
- [Examples](references/examples.md)
- [Deep FAQ](references/faq-deep.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to create local pipeline state files, snapshots, Markdown reports, and HTML visualizations when the included commands are run.]

## Skill Version(s):

5.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
