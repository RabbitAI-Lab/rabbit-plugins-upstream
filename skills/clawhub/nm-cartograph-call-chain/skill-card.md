## Description: <br>
Traces execution paths through the code graph with criticality scoring and Mermaid charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to trace how functions and entry points propagate through a local codebase, inspect critical call paths, and produce call-chain summaries and Mermaid diagrams. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local codebase files to trace function calls and may expose sensitive implementation details in summaries or diagrams. <br>
Mitigation: Use it only on repositories the agent is authorized to inspect, and review generated call-chain output before sharing it. <br>
Risk: When gauntlet integration is available, the skill runs the local graph_query.py helper from the user's Claude plugins directory. <br>
Mitigation: Keep the gauntlet plugin trusted and up to date, and fall back to static search when the local graph helper is unavailable or untrusted. <br>


## Reference(s): <br>
- [Cartograph homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-cartograph-call-chain) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, code] <br>
**Output Format:** [Markdown with inline shell commands, indented call trees, criticality breakdowns, and Mermaid flowcharts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local codebase files and may invoke a local graph_query.py helper when the gauntlet plugin is installed.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
