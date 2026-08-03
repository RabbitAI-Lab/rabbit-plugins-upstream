## Description: <br>
Analyzes camera footage or video URLs for contactless estimates of heart rate, respiration, blood oxygen, and heart rate variability, returning structured reports and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit face-oriented video or a video URL to a cloud service for contactless vital-sign analysis and to retrieve prior analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face or video data and inferred vital-sign information are sent to configured LifeEmergence cloud services. <br>
Mitigation: Use only with informed consent, approved data handling, and a reviewed cloud-service configuration; do not treat outputs as professional medical measurements or diagnosis. <br>
Risk: The skill can silently create or reuse account identities and store tokens in the workspace data directory. <br>
Mitigation: Review workspace data storage before deployment, isolate workspaces by user or project, and remove or rotate local tokens when access should end. <br>
Risk: History queries can retrieve cloud reports associated with the active or default local identity. <br>
Mitigation: Use separate identities for separate users or projects and review report-access expectations before enabling history lookup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [JSON or Markdown-formatted text with analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save returned report text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence; artifact frontmatter lists 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
