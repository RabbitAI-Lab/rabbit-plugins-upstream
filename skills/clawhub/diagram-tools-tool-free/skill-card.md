## Description: <br>
图表工具基础版 helps an agent create and configure diagrams such as Mermaid flowcharts and sequence diagrams, Graphviz DOT graphs, mind maps, Gantt charts, pie charts, and basic data charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and individual users use this skill to ask an agent for diagram generation guidance, diagram source snippets, chart configuration, and export-oriented workflows for lightweight visualization tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Command-capable automation may execute shell commands while preparing or exporting diagrams. <br>
Mitigation: Review proposed commands before execution, run the skill in a limited workspace, and avoid granting broad filesystem or network permissions. <br>
Risk: Optional callbacks and external API access can send diagram content or metadata outside the local environment. <br>
Mitigation: Disable callbacks and networked actions unless they are required, and use only non-sensitive diagrams unless explicit consent and data handling controls are in place. <br>
Risk: API key configuration and caching can expose credentials or sensitive diagram content if handled carelessly. <br>
Mitigation: Use environment-managed secrets, never hard-code keys into diagram files or scripts, and clear caches when working with confidential material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/diagram-tools-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON examples, diagram source snippets, and shell command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured status, result, metadata, execution log, and error fields when describing outputs.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
