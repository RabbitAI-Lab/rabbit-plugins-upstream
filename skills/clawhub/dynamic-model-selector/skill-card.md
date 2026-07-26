## Description: <br>
Dynamically select the best AI model for a task based on complexity, cost, and availability in GitHub Copilot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mpelissari](https://clawhub.ai/user/mpelissari) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to classify a task prompt and choose a GitHub Copilot model that balances task complexity, coding needs, and cost sensitivity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Model availability and cost information may become outdated. <br>
Mitigation: Confirm current GitHub Copilot model availability and pricing before relying on a recommendation for operational use. <br>
Risk: Sensitive prompts passed as shell arguments may be retained in shell history. <br>
Mitigation: Avoid passing highly sensitive prompts directly as command-line arguments; use safer local handling when prompt content is confidential. <br>


## Reference(s): <br>
- [Available GitHub Copilot Models - Detailed Specs](references/models.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text recommendation with model, reason, and cost tier] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Model availability and cost guidance may become outdated as GitHub Copilot offerings change.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
