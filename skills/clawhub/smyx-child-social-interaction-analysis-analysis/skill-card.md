## Description: <br>
Analyzes fixed-camera kindergarten or early-education video to report child social-interaction events, pairwise frequency and duration, initiators, low-interaction candidates, and heatmaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External educators, early-education operators, and authorized child-care teams use this skill to analyze classroom or playground video for visual social-interaction statistics and trend reports. The outputs are educational reference material and should not be treated as psychological or medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's classroom or playground video and generated reports may contain highly sensitive child data and may be sent to configured remote services. <br>
Mitigation: Use only with proper authorization and consent, and establish explicit retention, deletion, encryption, and access-control procedures before deployment. <br>
Risk: The skill silently manages account identity, persists tokens, and supports historical report access. <br>
Mitigation: Confirm identity handling, token storage, and report-access controls are acceptable for the deployment environment before installing or running the skill. <br>
Risk: Low-interaction flags and social-behavior statistics can be misread as clinical or developmental diagnosis. <br>
Mitigation: Present outputs as visual behavior statistics and educational attention cues only; require qualified professional assessment for medical or developmental concerns. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with report links and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can list historical reports and can save analysis output to a caller-provided file path.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; SKILL.md frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
