## Description: <br>
Analyzes bathroom doorway or privacy-preserving silhouette video to detect elderly toilet entry and exit events, calculate continuous occupancy time, and alert when a stay exceeds the configured safety threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, nursing-home operators, and home-safety system developers use this skill to monitor toilet occupancy duration from privacy-preserving camera inputs and surface abnormal-stay alerts for human follow-up. It provides monitoring statistics and alerts, not medical diagnosis or rescue instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive bathroom-monitoring footage or URLs through cloud APIs. <br>
Mitigation: Use doorway-only or pre-blurred footage where possible, avoid credential-bearing URLs, and deploy only with informed consent from the monitored person or authorized caregivers. <br>
Risk: Cloud history queries and report links may expose sensitive elder-care records if access controls or retention practices are weak. <br>
Mitigation: Verify publisher retention, deletion, authentication, and access-control practices before use in a care environment. <br>
Risk: The skill silently creates or reuses persistent local or remote user identities and tokens. <br>
Mitigation: Review account association behavior before deployment and ensure operators understand how identities, tokens, and historical reports are created, reused, and revoked. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown summary with structured JSON analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can list cloud-hosted historical reports and export report links when requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
