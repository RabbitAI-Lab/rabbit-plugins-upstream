## Description: <br>
Analyzes pet carrier videos or video URLs through LifeEmergence services to estimate resting respiratory rate, flag rates above 40 bpm, and return a non-diagnostic monitoring report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze cat, dog, or other pet videos captured inside airline carriers or transport crates, producing respiratory-rate data, alerts, guidance, and report links for transport monitoring. The output is for health-reference monitoring and does not diagnose disease or provide treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media, video URLs, and analysis requests are sent to LifeEmergence cloud services, and remote video URLs may be fetched by that service. <br>
Mitigation: Use only media and URLs approved for cloud processing, avoid sensitive footage unless consent and retention expectations are clear, and review the service terms before installation. <br>
Risk: The skill can silently create or reuse a local identity and query cloud report history tied to that identity. <br>
Mitigation: Install only when account/session persistence is acceptable, review who can trigger history queries, and clear or rotate local identity state when changing users or workspaces. <br>
Risk: Backend tokens may be stored in a workspace SQLite database. <br>
Mitigation: Restrict workspace access, treat the database as sensitive credential storage, and remove persisted tokens when uninstalling or transferring the workspace. <br>
Risk: Respiratory-rate output may be mistaken for medical diagnosis or treatment advice. <br>
Mitigation: Present results as non-diagnostic monitoring information and direct users to veterinary professionals for medical decisions or urgent symptoms. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Pet Carrier Respiratory Rate API Documentation](references/api_doc.md) <br>
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with respiratory-rate findings, alerts, recommendations, history tables, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save results to a local output file; report content depends on input media quality and cloud service responses.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
