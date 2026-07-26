## Description: <br>
Reviews surgery and procedure coding by checking structured case records and candidate procedures against coding rules, chart evidence, and an optional medical LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical coding reviewers and healthcare operations teams use this skill to review structured medical records and proposed surgery or procedure codes against rule-library guidance and chart evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive medical record text can be sent to configurable external rule and LLM services. <br>
Mitigation: Use only approved endpoints, de-identify records before input, and disable LLM mode when external processing is not allowed. <br>
Risk: Prepared medical record text can be saved locally when save-prepared behavior is enabled. <br>
Mitigation: Avoid saving prepared records for real patient data unless storage, retention, and access controls are approved. <br>
Risk: Model and rule-service credentials may be exposed if passed directly on command lines or stored in logs. <br>
Mitigation: Prefer environment-based or secret-manager credential handling and avoid logging appkeys or rule-service keys. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-surgery-review) <br>
- [Medical model API endpoint](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON object with final_decision and reasoning fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Decisions are limited to pass, fail, or manual review; reasoning is concise and should not include chain of thought.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
