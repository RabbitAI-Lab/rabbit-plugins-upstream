## Description: <br>
Analyzes pet videos or media URLs with the Life Emergence remote service to reconstruct body shape, estimate Body Condition Score from 1 to 9, classify underweight, ideal, or overweight status, and return structured observation results without diagnosing disease or prescribing treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit cat, dog, or other pet video inputs for BCS-oriented body shape assessment, structured reporting, and cloud history lookup. It is intended for pet weight-management workflows in smart feeders, pet cameras, and pet health platforms, not for veterinary diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos, images, or media URLs are sent to the Life Emergence remote service for analysis. <br>
Mitigation: Use only media approved for external processing, avoid private or internal URLs, and confirm retention and cleanup expectations with the publisher before deployment. <br>
Risk: The skill can create or reuse a local identity, read a workspace smyx-api-key file, and store account tokens locally. <br>
Mitigation: Review local identity and token storage before installation, restrict workspace access, and remove stored credentials or local account data when no longer needed. <br>
Risk: History report lookup retrieves cloud report records linked to the resolved identity. <br>
Mitigation: Confirm the active identity before history queries and verify that cloud report access controls match the intended user or workspace. <br>
Risk: BCS scoring is visually estimated and may differ from hands-on veterinary assessment. <br>
Mitigation: Present results as weight-management observations only and route health decisions to a veterinarian. <br>


## Reference(s): <br>
- [Pet health analysis API reference](artifact/references/api_doc.md) <br>
- [SMYX analysis API reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown status text with structured JSON analysis results, report links, or an optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History queries return cloud report lists; analysis results are reference observations and not medical advice.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
