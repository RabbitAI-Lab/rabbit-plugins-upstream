## Description: <br>
Adds a causal reasoning layer for planning, logging, backfilling, and evaluating high-level agent actions with observable outcomes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oswalpalash](https://clawhub.ai/user/oswalpalash) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to add causal intervention planning, outcome logging, historical backfill, treatment-effect estimation, and counterfactual failure analysis to high-level agent actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent causal logs from broad email, calendar, message, and activity history without enough scoping or retention controls. <br>
Mitigation: Install only when persistent activity logging is intended; restrict domains and date ranges, delete temporary exports, and define retention rules before use. <br>
Risk: Backfill scripts can query local account tools such as gog and wacli and import communication history. <br>
Mitigation: Confirm which accounts and tools will be accessed, prefer explicit JSON exports over direct broad queries, and review generated logs before reuse. <br>
Risk: Predictions or treatment-effect estimates may be uncertain or misleading when historical data is sparse or confounded. <br>
Mitigation: Require explicit user approval for purchases, deployments, permission changes, financial actions, and communication-history imports, and escalate when uncertainty is high. <br>


## Reference(s): <br>
- [Do-Calculus Reference](references/do-calculus.md) <br>
- [Treatment Effect Estimation](references/estimation.md) <br>
- [Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON/JSONL examples, YAML configuration, Python code, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce persistent local causal logs and treatment-effect estimates from user-provided or tool-exported activity history.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
