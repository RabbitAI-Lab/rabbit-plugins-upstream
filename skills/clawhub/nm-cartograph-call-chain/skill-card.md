## Description: <br>
Traces execution paths through the code graph with criticality scoring and Mermaid charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to trace a function or entry point through a codebase, inspect call paths, produce Mermaid charts, and review criticality factors such as file spread, security sensitivity, external calls, test gaps, and depth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read project code and optionally use an existing gauntlet graph database or plugin to trace call flows. <br>
Mitigation: Install and run it only on repositories you are comfortable having analyzed. <br>
Risk: Call-chain analysis can be incomplete when gauntlet graph data is missing or stale. <br>
Mitigation: Build or refresh the gauntlet graph before graph-based tracing, or treat static-search fallback results as partial. <br>


## Reference(s): <br>
- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with shell command examples, indented call trees, Mermaid flowcharts, and criticality breakdowns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use existing gauntlet graph data when available; falls back to static code search.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
