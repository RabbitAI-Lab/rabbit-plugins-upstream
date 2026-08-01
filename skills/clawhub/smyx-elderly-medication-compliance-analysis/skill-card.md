## Description: <br>
Analyzes fixed-camera medication-area images or videos to detect pick-up, to-mouth, and swallow steps and report medication-compliance status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, elder-care operators, and developers use this skill to analyze medication-area video or image inputs, detect whether the pick-up, to-mouth, and swallow steps occurred, and produce compliance reports or history listings for follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may upload medication-area video or video URLs containing sensitive home health footage to an external service. <br>
Mitigation: Use only with informed consent from the monitored person or authorized caregiver, and review the external service and report-retention practices before deployment. <br>
Risk: The skill queries cloud-stored medication-compliance history. <br>
Mitigation: Limit use to authorized caregivers or operators and verify that cloud history access, retention, and sharing are acceptable for the deployment. <br>
Risk: The skill can create or reuse a persistent local identity and store service tokens in a workspace SQLite database. <br>
Mitigation: Protect the workspace, avoid shared or untrusted runtimes, and clear local identity or token storage when access should be revoked. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown or JSON containing structured medication-step detection results, compliance status, confidence, alert text, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
