## Description: <br>
Ads Brain Planning Pipeline defines a content-layer planning flow for advertising agents, including create/optimize routing, conversation-state recognition, gate validation, unified outputs, and future integration guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lizejia668-code](https://clawhub.ai/user/lizejia668-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to guide advertising planning agents through campaign creation, optimization, unsupported-request handling, gate validation, and consistent next-action outputs. It is intended as planning guidance and does not directly execute advertising changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Downstream systems could turn planning guidance into live advertising campaign changes. <br>
Mitigation: Require clear user confirmation and business guardrails before any downstream system creates or modifies campaigns. <br>
Risk: Incorrect create/optimize routing or gate-validation output could mislead planning workflows. <br>
Mitigation: Review the generated plan and validation fields before deployment, especially capability, gate_validation, warnings, and next_action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lizejia668-code/skills/ads-brain-planning-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, markdown, code] <br>
**Output Format:** [Markdown guidance with JSON output schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines capability, conversation_state, gate_validation, warnings, next_action, and create/optimize output structures.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
