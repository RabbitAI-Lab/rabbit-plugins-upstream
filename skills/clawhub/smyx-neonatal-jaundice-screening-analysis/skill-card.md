## Description: <br>
Analyzes newborn face images or short videos through a cloud service to return a visual jaundice risk hint based on sclera color and facial skin yellowness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, clinicians, and developers use this skill to submit newborn face images or short videos for cloud-based visual jaundice pre-screening and to retrieve historical screening reports. The results are risk hints and report links, not a substitute for clinician evaluation or bilirubin measurement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Newborn images, video URLs, report queries, and report links may contain sensitive infant health data and are sent to the LifeEmergence cloud service. <br>
Mitigation: Use only with guardian consent; confirm the publisher's retention, authorization, deletion, and access-control practices before using real infant health data. <br>
Risk: The skill can create or reuse a local identity and cached tokens in the workspace. <br>
Mitigation: Run it in a controlled workspace, protect or remove local identity and token files after use, and avoid shared machines for real health data. <br>
Risk: Visual jaundice screening can be misleading under poor lighting, filters, face occlusion, or warm yellow light and is not a medical diagnosis. <br>
Mitigation: Capture clear newborn face media in natural white light and route medium, high, inconclusive, or persistent abnormal results to a clinician for bilirubin measurement. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/18072937735) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Structured JSON or Markdown report text with risk level, confidence, recommended action, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a file when an output path is supplied; history queries return cloud report records.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
