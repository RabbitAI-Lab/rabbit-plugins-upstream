## Description:

Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, determines whether a call is fraudulent, assesses risk level, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, security teams, and developers use this skill to analyze call recordings, call transcript text, local files, or URLs for suspected fraud patterns and receive structured risk findings, anti-fraud advice, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied media, files, URLs, and text may be processed by remote cloud services.

Mitigation: Use only with non-sensitive inputs unless the publisher documents the remote services, retention behavior, and supported input handling.

Risk: Automatic identity association, history lookup, and local token persistence may affect privacy or workspace state.

Mitigation: Review identity and token handling before installation, and avoid private or production workspaces until the publisher documents the identity model.

Risk: Fraud-call analysis results may be incomplete or incorrect.

Mitigation: Treat the report as advisory anti-fraud support and escalate suspected fraud through official security or law-enforcement channels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON structured analysis report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk level, detected fraud script patterns, prevention guidance, history report listings, and report links.]

## Skill Version(s):

9.9.14 (source: server release metadata; SKILL.md frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
