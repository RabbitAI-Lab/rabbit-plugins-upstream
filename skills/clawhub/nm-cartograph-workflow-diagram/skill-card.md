## Description: <br>
Generates a Mermaid workflow diagram showing process steps, decisions, and state transitions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn codebase workflows, CI/CD pipelines, lifecycle processes, and state machines into concise Mermaid flowcharts for documentation and review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected code or workflow details may be summarized into a Mermaid diagram and sent to the configured Mermaid rendering MCP. <br>
Mitigation: Limit the requested scope when the repository contains private or sensitive process information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-workflow-diagram) <br>
- [ClawDIS homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, guidance] <br>
**Output Format:** [Markdown with Mermaid flowchart code and a brief rendered-diagram description] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Limits diagrams to 20 nodes and retries Mermaid rendering up to two times.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
