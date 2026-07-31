## Description: <br>
Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, assesses whether a call is fraudulent, estimates risk level, and generates an Anti-Fraud Guardian analysis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and security teams use this skill to analyze call recordings, call text, or media URLs for fraud indicators and receive structured anti-fraud reports, risk levels, recommendations, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive call text or media may be uploaded to external services for processing. <br>
Mitigation: Use only with content the user is permitted to share, and review remote processing expectations before installation. <br>
Risk: The skill may silently create or reuse an account identity and retain identity or token data locally. <br>
Mitigation: Install only in trusted, isolated workspaces and clear local identity or token state when persistent account linkage is not desired. <br>
Risk: Cloud-stored history may be queried for the resolved identity. <br>
Mitigation: Limit use to trusted users and review history-query output before exposing it further. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON text with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns structured fraud-risk analysis, recommendations, history-list output, and report/export links when available.] <br>

## Skill Version(s): <br>
9.9.12 (source: server release metadata; artifact frontmatter lists 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
