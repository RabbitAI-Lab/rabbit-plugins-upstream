## Description: <br>
Extracts structured resident health records and a natural-language summary from unstructured clinical notes, physical exam reports, or questionnaire text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Public health staff at community health service centers and township clinics use this skill to turn de-identified resident health text into draft structured health records for professional review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive medical text and sends it to a remote LLM endpoint. <br>
Mitigation: Use only de-identified inputs and verify that the configured LLM endpoint is approved for the organization before use. <br>
Risk: The skill's privacy controls are under-scoped and should not be relied on to remove direct identifiers. <br>
Mitigation: Remove names, ID numbers, phone numbers, addresses, and other direct identifiers before invoking the skill. <br>
Risk: Writing output to a file can create a protected copy of sensitive health information. <br>
Mitigation: Use --output only in protected storage locations with appropriate access controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-health-record-management) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files] <br>
**Output Format:** [JSON health-record structure followed by a natural-language summary; optionally written to an output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Missing fields are represented as null, and generated records require review by public health staff before formal use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
