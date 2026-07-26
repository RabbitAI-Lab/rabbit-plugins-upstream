## Description: <br>
Agent Audit scans OpenClaw configuration and available model metadata to produce a markdown cost-optimization report with model-tier guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sharbelayy](https://clawhub.ai/user/sharbelayy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers managing OpenClaw agents use this skill to review model choices, estimate cost exposure, and generate suggested cost-optimization changes for manual review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated report may expose sensitive local agent names, model choices, or configuration details if shared. <br>
Mitigation: Review the report before sharing it outside the intended team. <br>
Risk: The skill should be treated as a lightweight configuration report rather than a complete ROI audit. <br>
Mitigation: Use recommendations as manual review inputs and confirm cost or ROI decisions against provider billing data. <br>
Risk: The --output option can create or overwrite the path supplied by the user. <br>
Mitigation: Write reports only to a safe path that the user intends to create or replace. <br>


## Reference(s): <br>
- [Agent Audit on ClawHub](https://clawhub.ai/sharbelayy/agent-audit) <br>
- [Model Pricing Reference](references/model-pricing.md) <br>
- [Task Classification Heuristics](references/task-classification.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report or plain-text summary with optional saved report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only audit output; saved reports may include local agent names, model choices, and cost estimates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
