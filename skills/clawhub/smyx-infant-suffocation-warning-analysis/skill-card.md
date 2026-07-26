## Description: <br>
Identifies prone sleeping positions, head covering, and occlusion of the mouth/nose by bedding or clothing; provides real-time high-risk alerts to safeguard infant sleep safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this skill to analyze infant sleep monitoring videos or URLs for prone sleeping, head covering, and mouth or nose occlusion risks, then receive structured safety alerts and report links. It can also query cloud-stored historical warning reports associated with the internally resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill sends infant sleep videos or video URLs to the LifeEmergence backend. <br>
Mitigation: Use it only with consent and privacy review for infant video data, and avoid submitting sensitive media unless remote processing is acceptable. <br>
Risk: The security evidence says the skill creates or reuses an internal identity, stores local account tokens, and queries cloud-stored historical reports. <br>
Mitigation: Treat report history and identity association as privacy-sensitive state; review token storage, account separation, and report access controls before deployment. <br>
Risk: The security evidence reports mismatched backend documentation, and the artifact describes the skill as an auxiliary monitoring tool. <br>
Mitigation: Confirm the configured backend endpoints and API behavior before use, and present alerts as assistive safety information that does not replace adult supervision or professional care. <br>


## Reference(s): <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with risk findings, safety suggestions, historical report tables, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video files, video URLs, sensitivity levels 1-5, basic/standard/json detail modes, and optional output files.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
