## Description:

Orchestrates multi-agent pipelines with DAG scheduling, shared state, recovery workflows, execution reporting, approval steps, visualization, a local dashboard, and MCP tool exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to define, validate, execute, resume, and report on multi-agent DAG pipelines for collection, analysis, approval, and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local web dashboard exposes pipeline data too broadly and has unsafe file-read and HTML injection issues according to the security summary.

Mitigation: Use the dashboard only with trusted local pipeline directories, keep it bound to localhost, and fix path containment and HTML escaping before sensitive workflows.

Risk: Pipeline task outputs are stored on disk and can include sensitive workflow data.

Mitigation: Avoid placing secrets or private account data in pipeline outputs, restrict access to state and report files, and remove retained state when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/multi-agent-orchestrator)
- [DAG scheduling guide](artifact/references/dag-scheduling-guide.md)
- [State sharing protocol](artifact/references/state-sharing-protocol.md)
- [Error recovery patterns](artifact/references/error-recovery-patterns.md)
- [Usage examples](artifact/references/examples.md)
- [Deep FAQ](artifact/references/faq-deep.md)
- [Anti-patterns](artifact/references/anti-patterns.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local pipeline state, reports, HTML visualizations, dashboard views, and MCP tool responses when the supporting scripts are used.]

## Skill Version(s):

5.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
