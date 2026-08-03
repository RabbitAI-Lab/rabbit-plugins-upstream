## Description: <br>
Analyzes authorized child surveillance images or video through a cloud service to identify negative emotions such as crying, anger, fear, and distress, returning structured report results and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, childcare operators, and developers use this skill to submit authorized child monitoring media or URLs for emotion analysis and to retrieve cloud-hosted historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's surveillance media and historical report data are processed by the LifeEmergence cloud service. <br>
Mitigation: Use the skill only with clear legal authority and consent, and only in environments where the LifeEmergence service is approved for this data. <br>
Risk: The skill silently manages identity and tokens, including fallback default identities. <br>
Mitigation: Use a dedicated workspace or account, avoid shared default identities, and review token and report retention or deletion controls before deployment. <br>
Risk: Network media URLs may point to footage the operator is not authorized to process. <br>
Mitigation: Submit only verified, authorized camera or media URLs and avoid arbitrary third-party URLs. <br>


## Reference(s): <br>
- [Child Emotion Recognition API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Error Reference](skills/smyx_analysis/references/api_doc.md) <br>
- [LifeEmergence Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Listing](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Structured text or JSON with report summaries, risk or recognition results, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media paths, public media URLs, historical report listing, and optional file output.] <br>

## Skill Version(s): <br>
1.0.18 (source: server release metadata; artifact frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
