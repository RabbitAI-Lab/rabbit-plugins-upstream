## Description:

Generates a Mermaid workflow diagram showing process steps, decisions, and state transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to map CI/CD pipelines, lifecycle processes, state machines, and other multi-step workflows into concise Mermaid flowcharts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to inspect project files and workflow details that include private operational information.

Mitigation: Keep the requested scope narrow and avoid running it across repositories or paths that contain sensitive workflows unless that disclosure is acceptable.

Risk: Generated Mermaid diagram content may be sent to a Mermaid rendering MCP.

Mitigation: Review diagram content before rendering when workflows include confidential project names, internal systems, or sensitive process details.

## Reference(s):

- [Workflow Diagram ClawHub Page](https://clawhub.ai/athola/skills/nm-cartograph-workflow-diagram)
- [Cartograph Source Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown with Mermaid code and a brief prose summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mermaid flowcharts are limited by the skill guidance to 20 nodes maximum and may be rendered through a Mermaid Chart MCP.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
