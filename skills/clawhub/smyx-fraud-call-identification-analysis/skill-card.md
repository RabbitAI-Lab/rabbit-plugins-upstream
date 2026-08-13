## Description:

Analyzes incoming call content for multi-dimensional risk, intelligently identifies scam scripts, determines if a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, security teams, and developers use this skill to submit call audio, call text, or a call recording URL for fraud-risk analysis. It returns a structured Anti-Fraud Guardian report with risk level, suspected fraud patterns, prevention guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call recordings, call text, URLs, and report history may be sent to lifeemergence.com services for analysis and retrieval.

Mitigation: Use only inputs whose data handling is approved for that service, and avoid sensitive recordings unless those terms are acceptable.

Risk: The skill creates or reuses a hidden local/cloud identity and can retrieve cloud report history associated with it.

Mitigation: Run it in a controlled workspace, review identity handling before deployment, and clear local state when changing users.

Risk: Tokens may be stored in a local workspace database.

Mitigation: Restrict workspace file access, avoid sharing the workspace database, and rotate or revoke credentials if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Fraud analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON report text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a user-specified file; history queries return a Markdown table derived from cloud report results.]

## Skill Version(s):

9.9.13 (source: ClawHub release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
