## Description: <br>
Generates pharmaceutical medical affairs academic material drafts from supplied material type, topic, audience, key messages, evidence points, and references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical affairs teams and supporting developers use this skill to generate structured first drafts of academic materials for clinical or scientific audiences. Outputs require medical, compliance, and subject-matter expert review before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Entered topics, key messages, evidence points, references, and extracted document content are sent to a remote medical model API. <br>
Mitigation: Use only with organizational approval for that endpoint and avoid PHI, patient identifiers, unpublished study data, or confidential commercial material unless an approved processing arrangement is in place. <br>
Risk: Generated academic medical drafts may be incomplete, inaccurate, or unsuitable for regulated use without review. <br>
Mitigation: Require medical, compliance, and subject-matter expert review before using outputs in external, promotional, clinical, or regulatory contexts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-academic-material-generation) <br>
- [Scientific Writing source skill](https://agent-skills.md/skills/ovachiever/droid-tings/scientific-writing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [UTF-8 JSON containing structured fields and Markdown text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an app key for the disclosed remote medical model API; optional preprocessing supports JSON, text, tables, documents, PDFs, and images when dependencies are available.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
