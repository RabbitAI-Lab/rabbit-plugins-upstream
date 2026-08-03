## Description: <br>
Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods. It is suitable for night-time safety monitoring in nursing homes and for elderly people living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, family caregivers, and agent workflows use this skill to analyze night-time elder-care images or videos for bed-exit, wandering, and extended immobility events. It can also query cloud-hosted historical monitoring reports for the associated user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elder-care images, videos, report queries, and identity values may be sent to external Life Emergence cloud services. <br>
Mitigation: Use only with approved footage, documented consent, and an organizational review of privacy, retention, and deletion requirements. <br>
Risk: The skill may silently create or reuse identities and store tokens locally. <br>
Mitigation: Run it only in managed environments where local token storage and generated or reused identities are acceptable and can be audited. <br>
Risk: Monitoring results are safety-care references and may be incomplete or incorrect. <br>
Mitigation: Require caregiver or operator review before treating alarms or reports as confirmed incidents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Structured analysis report text or JSON, with Markdown tables for historical report listings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include monitoring results, risk notes, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata; SKILL.md frontmatter states 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
