## Description: <br>
Detects the appearance of strangers near minors and actively issues safety reminder alerts to protect minor safety, suitable for homes, schools, childcare centers, and other scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to analyze monitoring images, videos, local files, or URLs for stranger proximity near minors, receive structured safety reports, and query cloud-hosted historical alert reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitoring images or videos and identifiers are sent to cloud services for processing. <br>
Mitigation: Use only where cloud processing is approved, consent and retention requirements are understood, and the documented service endpoints are acceptable. <br>
Risk: The skill can silently create or reuse an account-linked identity and store identity or auth material locally. <br>
Mitigation: Review identity handling before installation and prefer a version that asks for explicit consent before uploads, account creation, or credential storage. <br>
Risk: Safety-analysis outputs are advisory and may be incomplete or incorrect. <br>
Mitigation: Treat reports as safety reference material, keep human review in the workflow, and do not replace professional security or emergency procedures. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, JSON details, and shell command invocations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save results to a local output file and can list cloud-hosted historical reports.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; SKILL.md frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
