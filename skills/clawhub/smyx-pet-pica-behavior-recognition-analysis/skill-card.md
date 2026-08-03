## Description: <br>
Analyzes indoor pet-camera videos or URLs through cloud APIs to detect sustained contact between a pet's mouth and hazardous non-food objects and return warning-oriented structured reports without medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze indoor pet-monitoring videos for pica-like contact with wires, plastic, socks, tissues, toy fragments, and similar non-food hazards. It is intended for safety monitoring and alert-oriented reporting, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indoor camera footage may contain private household scenes and is sent to a lifeemergence cloud service for analysis. <br>
Mitigation: Use only footage that is appropriate to share with that service, avoid unrelated indoor scenes, and prefer a separate test workspace or account for evaluation. <br>
Risk: The skill silently creates or reuses a local identity and stores account tokens in the workspace data directory. <br>
Mitigation: Review local identity and token files before deployment, separate testing from production identities, and remove the local database or API-key file when the skill is no longer used. <br>
Risk: The reports are safety-monitoring outputs and may be mistaken for veterinary diagnosis. <br>
Mitigation: Present results as behavioral risk alerts and intervention suggestions only, and route health concerns to a qualified veterinarian. <br>


## Reference(s): <br>
- [Pet Pica Behavior API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, API Calls, Shell commands] <br>
**Output Format:** [Markdown and JSON structured reports with optional saved output files and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs warning-oriented pet safety findings, risk level details, intervention suggestions, and historical report listings when requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
