## Description: <br>
Detects architectural clusters and coupling boundaries via community detection on the code graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to identify module groupings, architectural boundaries, coupling hot spots, and refactoring targets in a codebase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Community and coupling findings can be incomplete or approximate when graph data is unavailable. <br>
Mitigation: Review the reported clusters against the source tree and build the graph data first when graph-backed analysis is expected. <br>
Risk: The skill may inspect local code structure and imports as part of its analysis. <br>
Mitigation: Run it only in repositories where that inspection is acceptable, and review shell commands before execution. <br>


## Reference(s): <br>
- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with shell commands, tables, warnings, Mermaid diagrams, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use an optional graph-query helper when available; otherwise falls back to directory and import analysis.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
