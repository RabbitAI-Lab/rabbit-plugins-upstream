## Description: <br>
Classifies likely infant cry causes from audio or audio-video input and returns confidence, secondary causes, acoustic feature summaries, directional soothing suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and product teams use this skill to connect baby-monitoring or parenting workflows to infant cry cause classification, historical report lookup, and structured caregiver-facing result summaries. Outputs should be treated as parenting support rather than medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive infant audio or video may be uploaded to a cloud service for processing. <br>
Mitigation: Use only with guardian consent, avoid unnecessary recordings, and confirm that cloud processing, retention, and access controls meet the deployment's privacy requirements. <br>
Risk: The skill may silently create or reuse account identity data and retrieve cloud history tied to that identity. <br>
Mitigation: Review identity handling before installation, isolate workspace state where needed, and confirm that history retrieval is appropriate for the user and environment. <br>
Risk: Cry cause classifications can be mistaken for medical conclusions. <br>
Mitigation: Present results as acoustic classification and directional soothing support only, and direct caregivers to professional care for persistent abnormal crying or concerning symptoms. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Infant Cry Cause Classification API Documentation](artifact/references/api_doc.md) <br>
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured text, with optional saved report files when an output path is provided.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces likely cry cause, confidence, secondary causes, cry duration, acoustic feature summary, soothing hint, history listings, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
