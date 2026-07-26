## Description: <br>
Supports medical record entity extraction, record-content quality control, clinical pathway quality control, and imaging report text quality control through a configurable medical model workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Healthcare application developers and medical workflow integrators can use this skill to run structured quality-control or extraction prompts over supplied medical record and report text. It is intended as model-assisted output and not as a formal diagnosis or clinical decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process sensitive medical record or report text. <br>
Mitigation: Install and run it only in environments approved for that data, and de-identify real patient records before use. <br>
Risk: The skill sends supplied text to a configured medical model API and requires an appkey for non-dry-run execution. <br>
Mitigation: Confirm the API endpoint and appkey handling meet the deployer's compliance and secret-management requirements. <br>
Risk: Standard output and --output files can contain the original question, metadata, and model answer. <br>
Mitigation: Treat logs and saved output files as sensitive artifacts and apply the same retention and access controls as the input data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-record-qc) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, configuration, guidance] <br>
**Output Format:** [JSON by default, with optional plain text model answers and NDJSON for batched records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include the original question, record metadata, task labels, model name, and model answer.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
