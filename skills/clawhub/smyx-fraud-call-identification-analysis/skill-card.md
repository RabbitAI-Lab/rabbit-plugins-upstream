## Description:

Analyzes incoming call content for multi-dimensional fraud risk, identifies scam scripts, assesses risk level, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, or security teams use this skill to submit call recordings, call-content text, or media URLs for fraud-call risk analysis and structured anti-fraud reporting. It can also retrieve server-side historical fraud-analysis reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call or media content, submitted URLs, report-history requests, and internal identity metadata may be sent to Life Emergence/Open API services.

Mitigation: Use only with content the user is authorized to submit, and review service scoping, consent, and retention expectations before deployment.

Risk: The skill silently manages identity and token state and may create a local SQLite account or token store.

Mitigation: Review local storage behavior, workspace data handling, and cleanup requirements before broad use.

Risk: The implementation is broader and more video-oriented than the fraud-call description.

Mitigation: Validate accepted input types and user-facing claims during release review so users understand what data may be processed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Fraud Analysis API Reference](references/api_doc.md)
- [Shared Analysis API Reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis results, with report links when returned by the remote service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local account or token state and may submit call/media content, URLs, report-history requests, and internal identity metadata to Life Emergence/Open API services.]

## Skill Version(s):

9.9.15 (source: server-resolved release metadata; skill frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
