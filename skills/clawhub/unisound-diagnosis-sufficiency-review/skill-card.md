## Description: <br>
Reviews whether requested diagnoses are sufficiently supported by structured medical record evidence and returns a diagnosis sufficiency decision. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical coding, DRG, and medical-record audit users can check whether candidate primary or other diagnoses are supported by case documentation. The skill provides audit support and does not provide medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive case text and the supplied model credential can be sent to a caller-configurable LLM endpoint. <br>
Mitigation: Install only in an environment approved for medical-record handling, use desensitized inputs, restrict --base to approved endpoints, and prefer --no-llm when external model sharing is not approved. <br>
Risk: Prepared medical-record text can be saved when --save-prepared is used. <br>
Mitigation: Use --save-prepared only with approved output locations, access controls, and retention handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-diagnosis-sufficiency-review) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Internal medical LLM endpoint](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON] <br>
**Output Format:** [JSON object with final_decision and reasoning; optionally saved as a JSON file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [final_decision is one of 依据充分, 依据不充分, or 待人工复核.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
