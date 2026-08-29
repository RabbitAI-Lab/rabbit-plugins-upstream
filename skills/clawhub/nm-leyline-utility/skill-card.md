## Description:

Scores agent actions by expected gain, cost, uncertainty, and redundancy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to decide whether to respond, retrieve, call tools, verify, delegate, or stop by scoring candidate actions against expected gain, cost, uncertainty, and redundancy. It is useful for gating expensive actions, choosing model tiers, continuing after partial results, and controlling agent dispatch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional prescriptive mode can influence when an agent calls tools or delegates work.

Mitigation: Use advisory mode by default and enable prescriptive gating only where utility-based control is intended.

Risk: Heuristic gain, uncertainty, and redundancy scores can mis-rank actions in high-impact workflows.

Mitigation: Require the action report breakdown and review low-confidence or high-cost decisions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-utility)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [State Builder](artifact/modules/state-builder.md)
- [Action Selector](artifact/modules/action-selector.md)
- [Integration](artifact/modules/integration.md)
- [Gain Estimation](artifact/modules/gain.md)
- [Step Cost](artifact/modules/step-cost.md)
- [Uncertainty Estimation](artifact/modules/uncertainty.md)
- [Redundancy](artifact/modules/redundancy.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with scoring formulas, action report templates, and optional YAML frontmatter settings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory scoring guidance by default; opt-in prescriptive mode can enforce utility-gated action selection.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
