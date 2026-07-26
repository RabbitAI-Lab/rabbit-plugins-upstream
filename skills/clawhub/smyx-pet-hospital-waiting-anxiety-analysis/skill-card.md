## Description: <br>
Analyzes pet hospital waiting-area video or image inputs through server-side APIs to identify anxiety-related behavior signals, assign a 1-5 anxiety level, and return a structured report without diagnosing disease or recommending treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External veterinary clinic staff and pet care operators use this skill to screen waiting-area media for pet anxiety indicators, prioritize high-stress pets for care or comfort, and review generated assessment reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Waiting-area media is uploaded to lifeemergence.com services and may include pets, owners, staff, or bystanders. <br>
Mitigation: Use only media that the clinic is authorized to share, avoid unnecessary bystander footage, and confirm provider retention and endpoint trust before deployment. <br>
Risk: The skill automatically creates or reuses an internal user identity and ties cloud history/report records to that identity. <br>
Mitigation: Deploy with clear account ownership expectations and review cloud report access controls before enabling history queries. <br>
Risk: Service tokens are stored in a local workspace SQLite database. <br>
Mitigation: Restrict workspace access, avoid sharing generated local state, and rotate or clear tokens according to the provider's operational guidance. <br>
Risk: Anxiety scoring may be affected by video quality, occlusion, camera angle, breed traits, or individual pet differences. <br>
Mitigation: Treat the output as workflow support only and require staff to combine results with direct observation and clinical judgment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with observed signals, anxiety level, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can list cloud history reports and can write the analysis output to a local file when requested.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
