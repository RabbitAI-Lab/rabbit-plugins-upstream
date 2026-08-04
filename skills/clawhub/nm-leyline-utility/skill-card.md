## Description: <br>
Scores agent actions by expected gain, cost, uncertainty, and redundancy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to score candidate actions before responding, retrieving, calling tools, verifying, delegating, or stopping. It helps control unnecessary tool use and premature stopping in advisory orchestration workflows, with prescriptive gating available only when a consuming skill opts in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A consuming skill that enables prescriptive utility gating can make this framework control whether an agent responds, retrieves, calls a tool, verifies, delegates, or stops. <br>
Mitigation: Review any consuming skill that sets utility_gated: true and use advisory mode unless mandatory gating is intentional. <br>
Risk: The scoring framework relies on heuristic self-estimates for gain and uncertainty, so scores can be misleading when evidence is incomplete or poorly calibrated. <br>
Mitigation: Require the agent to log the score breakdown and rationale, and review high-impact decisions before acting on them. <br>


## Reference(s): <br>
- [Utility skill on ClawHub](https://clawhub.ai/athola/skills/nm-leyline-utility) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [State Builder](modules/state-builder.md) <br>
- [Action Selector](modules/action-selector.md) <br>
- [Integration](modules/integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with scoring formulas, tables, YAML snippets, and action-report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory or opt-in prescriptive action-selection guidance; it does not include executable code.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
