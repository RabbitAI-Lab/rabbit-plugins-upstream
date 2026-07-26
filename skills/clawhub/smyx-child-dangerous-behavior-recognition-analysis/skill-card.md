## Description: <br>
Detects climbing, playing with fire, touching power sources, and dangerous actions near windows, providing real-time alerts for child safety supervision in homes, kindergartens, and nurseries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze child monitoring videos or video URLs for hazardous behaviors, receive structured safety reports, and query historical analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child media may be uploaded or provided by URL to external cloud services for analysis. <br>
Mitigation: Use only footage approved for that service, confirm consent and retention requirements, and avoid sending media that violates local privacy rules. <br>
Risk: The skill can create or reuse persistent identity and token data while associating analysis reports with that identity. <br>
Mitigation: Run it only in governed workspaces where local token storage, identity creation, and report association are acceptable and periodically review stored credentials. <br>
Risk: Historical report queries can retrieve prior child-safety analysis reports from the cloud service. <br>
Mitigation: Limit access to trusted operators and verify that report visibility and retention align with the deployment's privacy requirements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown report text with optional JSON detail, historical report listings, and report export links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an output file when --output is supplied; supports mp4, avi, and mov files up to 10 MB or video URLs.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
