## Description:

Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, determines whether a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, security teams, and developers use this skill to analyze call recordings, call text, local files, or URLs for fraud-call indicators and receive a structured risk report with recommendations and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill sends call content, uploaded files, URLs, identity-linked report data, and generated history reports to a configured cloud service.

Mitigation: Use only when the operator is comfortable sending that data to the configured service, and avoid highly sensitive calls unless the publisher provides clear privacy, retention, and token-storage terms.

Risk: The security evidence flags under-disclosed cloud processing, automatic identity/account handling, and local token persistence for sensitive call and file data.

Mitigation: Review the publisher's data-handling terms and run the skill in an environment where token storage and account-linked report history are acceptable.

## Reference(s):

- [Fraud Call Identification API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and structured JSON returned by command-line scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return analysis results, risk guidance, report export links, or historical report lists.]

## Skill Version(s):

9.9.17 (source: ClawHub release metadata; artifact frontmatter version is 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
