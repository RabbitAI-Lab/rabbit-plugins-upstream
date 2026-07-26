## Description: <br>
Orchestrates local multi-agent pipelines with DAG validation, shared state, retries, resume support, execution reports, Gantt visualization, approval gates, hardware-aware recommendations, update checks, and dynamic control flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to define, validate, and step through local multi-agent DAG workflows, including conditionals, branch routing, retries, approvals, reports, and resume flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved state, error messages, and generated reports can contain sensitive node outputs. <br>
Mitigation: Do not store secrets in node outputs or error messages, and keep state and report files in deliberate, access-controlled locations. <br>
Risk: Untrusted pipeline JSON can drive misleading workflow behavior or unwanted local state and report outputs. <br>
Mitigation: Use trusted pipeline definitions, review DAG files before execution, and choose state and report paths deliberately. <br>
Risk: Generated HTML reports may include content supplied by pipeline nodes. <br>
Mitigation: Review generated HTML reports before opening or sharing them when pipeline content comes from someone else. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/multi-agent-orchestrator) <br>
- [DAG scheduling guide](references/dag-scheduling-guide.md) <br>
- [State sharing protocol](references/state-sharing-protocol.md) <br>
- [Error recovery patterns](references/error-recovery-patterns.md) <br>
- [Anti-patterns](references/anti-patterns.md) <br>
- [Examples](references/examples.md) <br>
- [Deep FAQ](references/faq-deep.md) <br>
- [Pipeline DAG template](templates/pipeline_dag_template.json) <br>
- [Dynamic control flow template](templates/control_flow_template.json) <br>
- [State schema](templates/state_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON pipeline and state files, Python shell commands, Markdown execution reports, and HTML Gantt reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local JSON state and report files; generated reports may contain node output data.] <br>

## Skill Version(s): <br>
4.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
