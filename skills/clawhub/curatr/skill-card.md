## Description: <br>
HealthClaw Curatr evaluates patient FHIR R4 US Core health records for coding and structural issues, presents plain-language feedback, validates codes through public terminology APIs, and supports patient-approved corrections or provider correction requests with provenance tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patient-facing health data assistants and healthcare application developers use Curatr to review FHIR records for outdated codes, missing fields, and terminology mismatches, then present understandable correction options to the patient. It also supports applying only patient-approved fixes or preparing a provider correction request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle sensitive medical data and may use public terminology services for validation. <br>
Mitigation: Avoid sending unnecessary patient details to terminology services and confirm what data leaves the FHIR environment before use. <br>
Risk: Approved corrections can write changed health-record data. <br>
Mitigation: Confirm the target FHIR store and require explicit patient confirmation before applying any correction. <br>
Risk: Write access depends on a step-up secret. <br>
Mitigation: Keep STEP_UP_SECRET private and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Curatr ClawHub Skill Page](https://clawhub.ai/aks129/skills/curatr) <br>
- [HL7 Public FHIR Terminology Server](https://tx.fhir.org) <br>
- [NLM Clinical Tables API](https://clinicaltables.nlm.nih.gov) <br>
- [RxNav API](https://rxnav.nlm.nih.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces issue descriptions, impact summaries, suggested fixes, updated FHIR resources with Provenance records, and structured provider correction requests; write actions require step-up and human confirmation.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
