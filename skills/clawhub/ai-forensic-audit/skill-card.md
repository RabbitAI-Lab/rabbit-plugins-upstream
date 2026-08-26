## Description:

AI Forensic Audit guides agents through a five-step provenance audit of AI-generated content, agent actions, or conversation records, producing an evidence chain, confidence rating, risks, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

External users, auditors, and developers use this skill to structure AI provenance, content attribution, agent compliance, leak-tracing, and high-stakes AI response audits from supplied evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad audit and provenance trigger words could invoke the skill more often than intended.

Mitigation: Use the skill only for intentional AI evidence-chain audit requests and review the generated report before acting on it.

Risk: Audit materials may include sensitive logs, personal data, or confidential records.

Mitigation: Provide only evidence necessary for the audit scope and redact sensitive data that is not needed for the report.

Risk: Incomplete or weak evidence can lead to overconfident attribution or compliance conclusions.

Mitigation: Preserve evidence gaps in the report, use the skill's L1-L4 confidence framing, and require qualified review for legal, regulatory, medical, or other high-stakes conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-forensic-audit)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown audit report with evidence lists, verification matrix, confidence level, risks, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable behavior; markdown-only guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
