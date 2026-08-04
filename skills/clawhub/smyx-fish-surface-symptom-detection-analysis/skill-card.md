## Description: <br>
Through fixed cameras on aquariums or underwater cameras capturing high-definition fish images, the system uses AI vision analysis to detect abnormal symptoms on the fish body surface: white-spot disease, hyperemia, and fin-rot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and aquaculture application developers use this skill to analyze fish images or videos for visible surface symptoms, receive structured health reports, and query related cloud history reports. The results are visual screening guidance only and should be reviewed by an appropriate aquarium or aquatic veterinary professional before treatment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fish images, videos, or media URLs are sent to LifeEmergence cloud services for analysis. <br>
Mitigation: Use the skill only with media that the user is permitted to share with the cloud service, and avoid submitting sensitive or unauthorized aquarium footage. <br>
Risk: Requests are associated with an internally managed identity and the skill can query account-linked cloud history. <br>
Mitigation: Review the active identity before using history features, and avoid running history queries when prior cloud reports should not be reused or exposed. <br>
Risk: The skill stores or reuses identity and token records in the workspace data directory. <br>
Mitigation: Review or remove data/smyx-api-key.txt and local SMYX database files before installation or use when identity reuse is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis) <br>
- [Fish surface symptom API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-oriented analysis text with JSON-capable structured result data, command examples, optional saved output files, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include symptom classifications, confidence values, affected locations, severity, recommended actions without specific medication instructions, disclaimers, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
