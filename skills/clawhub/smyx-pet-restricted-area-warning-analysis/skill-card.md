## Description: <br>
Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts for home pet monitoring scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners and home-monitoring operators use this skill to analyze pet monitoring images or videos for restricted-area entry, dining-table climbing, and trash-rummaging behavior. It returns structured warning results, recommendations, and report links for follow-up review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Home pet-monitoring videos or video URLs may be uploaded to the vendor's cloud service for analysis. <br>
Mitigation: Use only with footage appropriate for vendor cloud processing, and confirm retention, deletion, and access controls before deployment. <br>
Risk: The skill can create or reuse an identity, retrieve cloud report history, and store account tokens locally. <br>
Mitigation: Review account handling and local token storage before installation, restrict runtime access, and remove stored credentials or history when no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Document](references/api_doc.md) <br>
- [SMYX Analysis API Document](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown reports and JSON structured analysis results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include alert status, behavior counts, recommendations, history tables, and report links.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
