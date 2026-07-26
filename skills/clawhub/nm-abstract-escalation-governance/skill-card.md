## Description: <br>
Assess whether to escalate models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when model escalation is justified, document the reason, and avoid unnecessary cost or latency from premature escalation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may influence an agent to use more capable and potentially more costly models. <br>
Mitigation: Require documented investigation, a bounded escalation scope, and a cost-benefit justification before changing model capability. <br>
Risk: Incorrect escalation guidance could cause unnecessary latency or missed escalation for genuinely complex tasks. <br>
Mitigation: Review the decision framework against local model policy and monitor escalations during rollout. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-escalation-governance) <br>
- [Source homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with checklists, decision criteria, and protocol steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no code execution, persistence, data access, or credential handling was identified by the security evidence.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
