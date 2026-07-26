## Description: <br>
图表工具基础版 helps an agent create Mermaid and Graphviz diagrams, including flowcharts, sequence diagrams, mind maps, architecture diagrams, and basic data charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn natural-language diagram requests into Mermaid or Graphviz content, basic chart configuration, and rendering guidance for lightweight personal workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram content or callback URLs may be sent outside the local environment because the release evidence says network/API behavior is not clearly scoped. <br>
Mitigation: Use the skill only for non-sensitive diagrams unless local-only rendering is confirmed, and require explicit confirmation before sending content or callback URLs to a service. <br>
Risk: The skill can propose shell commands for rendering, environment checks, or setup. <br>
Mitigation: Review commands before execution, run them only in trusted workspaces, and avoid exposing API keys, tokens, or secrets. <br>
Risk: The security evidence marks the release suspicious because its local-only privacy claim conflicts with unclear network/API behavior. <br>
Mitigation: Treat installation as review-required and keep sensitive diagrams, credentials, and private infrastructure details out of inputs until the behavior is verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/diagram-tools-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Mermaid, Graphviz DOT, JSON configuration, and inline shell or code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return structured status, result, and execution log fields; rendering behavior may depend on local runtimes or external APIs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
