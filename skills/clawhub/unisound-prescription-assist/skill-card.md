## Description: <br>
Helps primary care clinicians draft prescriptions by recommending medications, checking interactions and contraindications, and returning dose-adjustment guidance as JSON plus a natural-language summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Community clinic and primary care clinicians can use this skill for prescription-assistance drafts based on diagnoses, age, renal function, allergies, and concurrent medications. Its output is decision support and requires clinician review before use in care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient-related input is sent to a remote model, and the artifact does not enforce the de-identification promised in its documentation. <br>
Mitigation: Do not submit identifiable patient information unless the remote service, privacy basis, consent, retention, and governance controls have been approved; de-identify inputs before use. <br>
Risk: Prescription recommendations may be incomplete, incorrect, or unsuitable for a regulated clinical setting. <br>
Mitigation: Use the output only as clinical decision support and require review by a licensed clinician or pharmacist before prescribing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-prescription-assist) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Configured medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON followed by a natural-language summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an app key and sends prescription input to the configured remote medical model API.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
