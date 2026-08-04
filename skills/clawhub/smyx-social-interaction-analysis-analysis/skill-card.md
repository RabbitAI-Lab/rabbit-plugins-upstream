## Description: <br>
Analyzes multi-pet videos to classify social interactions such as sniffing, chasing, biting, fleeing, hiding, and playing, then returns a structured social-behavior report with durations, frequencies, initiators, receivers, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, pet boarding centers, pet daycare operators, and animal behavior clinics use this skill to submit multi-pet videos or URLs and receive structured observations about social behavior and possible conflict patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or URLs are processed by the LifeEmergence/SMYX cloud service. <br>
Mitigation: Use only footage you are permitted to upload, and review the service owner, retention policy, deletion path, and access controls before processing sensitive home, client, or facility footage. <br>
Risk: History reports are retrieved from the cloud and associated with the resolved account identity. <br>
Mitigation: Confirm that users understand report history is account-linked, and verify how to revoke access or delete stored reports before relying on the history feature. <br>
Risk: The skill may create or reuse a local identity and persist account tokens in the workspace data database. <br>
Mitigation: Run the skill in an isolated workspace when possible, and inspect or clear workspace data credentials after use in shared or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-social-interaction-analysis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet Social Interaction Analysis API doc](references/api_doc.md) <br>
- [SMYX Analysis API doc](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis payloads and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report-history listings and optional saved output files when requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter declares 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
