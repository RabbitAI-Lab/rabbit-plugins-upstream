## Description:

Analyzes incoming call content for multi-dimensional risk, identifies potential scam scripts, assesses risk levels, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and security teams can submit call recordings, URLs, or transcripts to review potential fraud patterns, risk levels, and prevention suggestions. The skill also retrieves prior analysis reports; its results are advisory and do not replace an official police determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release suspicious, citing a mismatch with its call-fraud purpose, account and identity handling, and safeguards that may not work as described; the security guidance also flags external media processing and export-only behavior for review.

Mitigation: Review the purpose, identity and data handling, media processing, export behavior, and stated safeguards before installing or relying on the skill.

Risk: Skillspector reports partial analysis because a local reference could not be resolved, so the security evidence is incomplete.

Mitigation: Resolve the missing reference and repeat the security review before relying on the skill.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Analysis API details](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report text or JSON, with risk level, prevention suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory fraud assessment; not a formal police determination.]

## Skill Version(s):

9.9.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
