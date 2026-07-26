## Description: <br>
Provides primary-care common disease advice from patient complaint, symptom, sign, and basic clinical text, returning differential diagnoses, recommended examinations, initial treatment advice, referral judgment, JSON, and a natural-language summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinicians and healthcare developers use this skill to generate structured common disease decision-support suggestions for community clinic cases. Outputs require review by a licensed clinician and are not a substitute for diagnosis or treatment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient case text may include sensitive health or identifying information that is sent to a remote model endpoint. <br>
Mitigation: Use only de-identified case text and verify the configured base endpoint and appkey handling before real clinical use. <br>
Risk: The documentation promises de-identification before model calls, but the reviewed implementation does not perform that redaction. <br>
Mitigation: Do not rely on the skill for de-identification until the implementation is fixed or an external redaction control is enforced. <br>
Risk: Medical advice output can be incorrect, incomplete, or unsuitable for a specific patient. <br>
Mitigation: Require review by a licensed clinician and treat the output as decision support rather than a diagnosis or treatment decision. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/unisound-llm/skills/unisound-common-disease-advice) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON followed by a natural-language summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Structured diagnosis candidates, recommended exams, treatment advice, warnings, referral status, and referral rationale.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
