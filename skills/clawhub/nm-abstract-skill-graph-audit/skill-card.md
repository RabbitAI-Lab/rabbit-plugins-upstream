## Description: <br>
Audit Skill() refs; detect hubs, isolates, and dangling targets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to audit OpenClaw skill reference graphs, find heavily referenced hubs and orchestrators, identify isolates, and catch dangling Skill() references before documentation, renaming, retirement, or release work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the referenced audit against a plugins root reads skill files under that path, which can expose private repository contents to the local report workflow. <br>
Mitigation: Run it only against repositories and plugin roots you intend to inspect, and review the referenced script or plugin before using it on private sources. <br>
Risk: The audit focuses on Skill(plugin:name) references and can miss unsupported reference forms or include documented examples as findings. <br>
Mitigation: Use the documented test-suite and smoke-check workflows, then review dangling references and isolates before making retirement or merge decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-graph-audit) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Usage reference](artifact/modules/usage.md) <br>
- [Interpretation guide](artifact/modules/interpretation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide text or JSON report generation through the referenced skill_graph.py workflow.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
