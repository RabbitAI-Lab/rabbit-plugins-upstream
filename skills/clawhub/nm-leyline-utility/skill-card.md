## Description: <br>
Scores agent actions by expected gain, cost, uncertainty, and redundancy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to score whether an agent should respond, retrieve information, call a tool, verify work, delegate, or stop. It is intended for cost-aware orchestration and verification decisions during multi-step agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may cause the skill to appear during general planning where utility scoring is unnecessary. <br>
Mitigation: Use the scoring checklist when there is a meaningful cost, uncertainty, redundancy, delegation, or verification decision; skip it for obvious single-step actions. <br>
Risk: A consuming skill that opts into utility_gated mode can strongly steer tool-use or delegation decisions. <br>
Mitigation: Keep advisory mode as the default unless prescriptive behavior is explicitly desired, and review logged utility breakdowns before relying on gated decisions. <br>
Risk: Heuristic scores can mis-rank actions when gain, uncertainty, or redundancy estimates are poorly calibrated. <br>
Mitigation: Require all score components in the action report, check termination conditions after each step, and document any high-gain override with the gain value. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-utility) <br>
- [ClawHub Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Action Selector](modules/action-selector.md) <br>
- [State Builder](modules/state-builder.md) <br>
- [Integration](modules/integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown guidance with utility scores and action reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces heuristic decision guidance; it does not execute tools or handle data directly.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
