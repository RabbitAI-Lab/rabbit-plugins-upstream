## Description: <br>
Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, determines whether a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and security teams use this skill to submit call recordings, call transcript text, or media URLs for fraud-risk analysis and structured anti-fraud reporting. It can also query cloud-hosted historical analysis reports linked to the internally resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Supplied files, URLs, and transcript text are sent to third-party lifeemergence.com services for remote analysis. <br>
Mitigation: Install and run the skill only when those remote data flows are acceptable for the content being analyzed. <br>
Risk: The skill can create or reuse an account-like identity, store tokens locally, and retrieve cloud-hosted historical reports associated with that identity. <br>
Mitigation: Review local token storage and cloud history behavior before use, and avoid shared environments where account-linked report history would be inappropriate. <br>
Risk: The artifacts are inconsistent about audio/text fraud-call support versus video/media analysis behavior. <br>
Mitigation: Validate expected input types and output behavior in a controlled environment before relying on results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Fraud Analysis API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-like structured text with report links; history queries return structured report lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.] <br>

## Skill Version(s): <br>
9.9.11 (source: ClawHub release metadata; SKILL.md frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
