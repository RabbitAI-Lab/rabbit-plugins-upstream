## Description: <br>
Generates personalized vaccination reminder lists from a resident's age, vaccination history, and special circumstances based on China's national immunization schedule. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Community health and township clinic staff use this skill to review resident vaccination records, identify overdue or upcoming vaccinations, and prepare reminder guidance for clinician review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resident health records may be sent to a remote model endpoint without enforced redaction or an explicit consent step. <br>
Mitigation: Use only after organizational approval of the endpoint; remove names, ID numbers, phone numbers, addresses, and other identifiers before input. <br>
Risk: Vaccination guidance can vary by region, record completeness, and patient-specific contraindications. <br>
Mitigation: Treat the output as reminder support and have a qualified vaccination clinician verify the final schedule and precautions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-vaccination-reminder) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Remote model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, text, guidance] <br>
**Output Format:** [JSON followed by a natural-language summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires resident vaccination input and an app key for the remote model API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
