## Description: <br>
Analyzes resting pet video from a fixed camera to estimate respiratory rate, compare it with species and body-size norms, and return abnormal-breathing warnings with report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, veterinary staff, and pet-care operators use this skill to analyze resting pet media for respiratory-rate abnormalities and retrieve cloud report history. Results are health-reference warnings, not veterinary diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs may be sent to LifeEmergence cloud services. <br>
Mitigation: Use only with informed user approval for cloud processing, avoid sensitive media, and prefer a version that clearly prompts before upload and documents retention and deletion. <br>
Risk: Reports may be tied to an automatically resolved or created identity with weak user control over account linkage and history lookup. <br>
Mitigation: Review identity-linking behavior before deployment and require clear controls for account linkage, report history access, and deletion. <br>
Risk: Service tokens may be stored in the workspace data directory. <br>
Mitigation: Restrict workspace access, avoid sharing workspaces that contain service tokens, and rotate or remove tokens when access is no longer needed. <br>
Risk: Respiratory-rate warnings could be mistaken for medical diagnosis. <br>
Mitigation: Present results as health-reference screening only and advise veterinary review for persistent, severe, or concerning symptoms. <br>


## Reference(s): <br>
- [Pet Respiratory API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report or JSON result from CLI/API, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include respiratory-rate findings, warning level, recommendations, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
