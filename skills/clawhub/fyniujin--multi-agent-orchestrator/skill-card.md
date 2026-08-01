## Description: <br>
Multi-Agent Pro helps agents define, validate, execute, resume, report on, and visualize multi-agent DAG workflows with shared local state, recovery controls, sub-pipeline reuse, and execution snapshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workflow authors use this skill to break complex work into coordinated agent pipelines, validate DAG structure, track node state, recover failed runs, and produce execution reports or visual timelines. It is best suited for local, file-based orchestration where the agent performs the task work and the bundled scripts provide workflow infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pipeline state, reports, snapshots, and history are stored on disk and can contain workflow inputs or node outputs. <br>
Mitigation: Avoid storing secrets or sensitive data in node outputs, keep generated artifacts in an appropriate local workspace, and review reports before sharing them. <br>
Risk: Snapshot restore can reset downstream workflow state and change later execution results. <br>
Mitigation: Use snapshot restore deliberately, confirm the selected restore point, and inspect downstream nodes before resuming execution. <br>
Risk: The skill supports local workflow orchestration but the agent still performs the substantive task work. <br>
Mitigation: Review generated DAGs, shell commands, and reports before execution or publication, especially when workflow outputs affect business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/multi-agent-orchestrator) <br>
- [DAG scheduling guide](references/dag-scheduling-guide.md) <br>
- [State sharing protocol](references/state-sharing-protocol.md) <br>
- [Error recovery patterns](references/error-recovery-patterns.md) <br>
- [Usage examples](references/examples.md) <br>
- [Control-flow and orchestration anti-patterns](references/anti-patterns.md) <br>
- [Deep FAQ](references/faq-deep.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON pipeline definitions, Markdown execution reports, HTML Gantt visualizations, local state files, and shell command sequences.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are local workflow artifacts; reports, snapshots, state files, and history may contain node outputs supplied during execution.] <br>

## Skill Version(s): <br>
5.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
