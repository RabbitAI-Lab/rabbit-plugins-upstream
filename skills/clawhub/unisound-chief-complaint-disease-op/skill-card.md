## Description: <br>
Checks outpatient medical records for chief complaints that improperly use disease or procedure names, using a configured HiVoice MaaS medical LLM endpoint to return a defect status and reason. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical quality teams use this skill to run a focused outpatient EMR quality-control rule over de-identified Chinese medical record text and save a local no-defect or defect-with-reason result for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outpatient record text may contain PHI or other sensitive medical information before it is sent to the configured LLM endpoint. <br>
Mitigation: Use only de-identified records, remove names and IDs before running the skill, and install it only where the endpoint is approved by the organization. <br>
Risk: The required app key could be exposed if committed, logged, or shared insecurely. <br>
Mitigation: Provide the app key at runtime through approved secret handling and do not write it into the repository or published artifact. <br>
Risk: Prepared input or result files may contain sensitive record content when saved locally. <br>
Mitigation: Avoid --save-prepared unless needed for an approved debugging workflow, store outputs in a secure location, and review files for sensitive content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-chief-complaint-disease-op) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [UTF-8 text file and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns no-defect or defect-with-reason text; requires de-identified input records and an app key.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
