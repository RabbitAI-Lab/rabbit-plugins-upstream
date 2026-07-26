## Description: <br>
Reviews whether structured medical-record evidence sufficiently supports listed surgeries or procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Healthcare coding, reimbursement, and audit teams use this skill to check whether inpatient record documents provide enough support for proposed surgery or procedure codes. Developers can run it as a CLI-backed review component connected to approved guideline and medical-model services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical records may contain sensitive personal or health information that is sent to configured guideline and model services. <br>
Mitigation: Install only in an authorized medical-record processing environment, prefer de-identified inputs, and keep guideline and model endpoints restricted to approved services. <br>
Risk: Prepared record text or output JSON can be saved locally when optional output paths or --save-prepared are used. <br>
Mitigation: Avoid saving PHI unless retention, filesystem access, and deletion controls are approved for the deployment. <br>
Risk: The review output is coding-audit support and may be incomplete or unsuitable for clinical decision-making. <br>
Mitigation: Use human review for final reimbursement, coding, or clinical decisions, especially when the result is 待人工复核 or 依据不充分. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-surgery-sufficiency-review) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Configured medical model API base](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Guidance] <br>
**Output Format:** [JSON object with final_decision and reasoning fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The final_decision value is one of: 依据充分, 依据不充分, or 待人工复核.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
