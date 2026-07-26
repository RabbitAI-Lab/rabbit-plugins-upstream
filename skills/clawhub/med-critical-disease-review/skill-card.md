## Description: <br>
Assesses structured inpatient medical records against 28 critical disease insurance claim criteria by calling an assessment API and returning raw JSON plus a natural-language conclusion with evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Claims reviewers and agents use this skill to evaluate critical disease insurance claim eligibility from structured inpatient medical records and summarize the decision evidence. It supports claim review workflows and is not medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive medical records are sent to the configured assessment API. <br>
Mitigation: Use this skill only when authorized to process the records with that service, and verify the API destination before use. <br>
Risk: API responses, text summaries, and prepared payload files can contain sensitive health data and may be written locally. <br>
Mitigation: Set output paths to protected locations, manage retention according to policy, and avoid --save-prepared unless it is needed. <br>
Risk: The privacy text claims de-identification and no local persistence, while the security evidence says the skill writes outputs locally. <br>
Mitigation: Do not rely on the skill alone for privacy controls; apply required de-identification and storage controls in the surrounding workflow. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/unisound-llm/skills/med-critical-disease-review) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Assessment service endpoint](https://skills-medical.hivoice.cn/api/v1/assessment/assess/{disease}) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands] <br>
**Output Format:** [Raw JSON response and natural-language text summary, optionally written to files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key and writes output files to configured paths; optional preprocessing can normalize supported document formats into medicalRecord JSON.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
