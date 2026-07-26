## Description: <br>
Guides agents through decision-tree analysis for multi-stage decisions with uncertain outcomes, estimated probabilities, quantified payoffs, rollback, sensitivity analysis, and EVPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to structure sequential decisions, make assumptions explicit, calculate expected values, and identify thresholds where recommendations change. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may over-rely on decision-tree outputs as financial or business advice. <br>
Mitigation: Treat outputs as decision-support guidance and verify probabilities, assumptions, payoffs, and source claims before relying on recommendations. <br>
Risk: Incorrect probabilities, inconsistent payoff units, or missing branches can produce misleading expected-value recommendations. <br>
Mitigation: Require documented probability bases, consistent payoff units, sensitivity analysis, EVPI checks, and an explicit missing-branch audit. <br>


## Reference(s): <br>
- [Decision Tree Sources](references/sources.md) <br>
- [Magee 1964 Chemical Plant Investment Example](examples/magee-1964-chemical-plant-investment-hbr.md) <br>
- [Eisenhower D-Day Weather Decision Example](examples/eisenhower-1944-d-day-weather-decision.md) <br>
- [Chipmaker Fab Investment Under AI Uncertainty Example](examples/chipmaker-leading-edge-fab-investment-2024-2026.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/decision-tree) <br>
- [deciqAI Decision Tree Page](https://www.deciqai.com/c/decision-tree) <br>
- [deciqAI Decision Tree Metadata](https://www.deciqai.com/s/decision-tree.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Analysis] <br>
**Output Format:** [Markdown decision-tree worksheet with tables, calculations, sensitivity thresholds, and a recommendation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided or estimated probabilities and consistent payoff units; no executable output.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
