## Description:

Review the quality, reproducibility, legal reasoning, and decision usefulness of an existing freedom-to-operate (FTO), patent-infringement-risk, or event IP risk report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP, legal, product, and diligence teams use this skill to audit existing FTO or patent-risk reports for evidence quality, reproducibility, legal reasoning, decision usefulness, omissions, fatal defects, and remediation needs. It supports report-quality review and decision support; it does not replace a jurisdiction-specific legal opinion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewed FTO reports and product details may contain sensitive legal, product, or commercial information.

Mitigation: Treat supplied materials as confidential and use optional PatSnap connectors only when sending the relevant search queries and patent-review context to configured services is acceptable.

Risk: Generated assessments may be mistaken for legal advice or relied on without qualified review.

Mitigation: Review outputs with qualified counsel and responsible business owners before using them for material legal or commercial decisions.

Risk: Independent-search overlap, omissions, or empty result sets may be overread as proof of complete recall or no patent risk.

Mitigation: Report observed coverage and limitations explicitly, keep pending applications separate, and use any recall estimate only as a documented qualified heuristic.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/review-fto-report-quality-ip)
- [FTO Report Quality Review](https://open.patsnap.com/marketplace/skill-hub/fto-report-quality)
- [FTO Report Quality Standards](artifact/references/fto-quality-standards.md)
- [FTO Report Quality Assessment Checklist](artifact/references/assessment-checklist.md)
- [Independent Verification Guide for FTO Report Review](artifact/references/independent-verification-guide.md)
- [Harness Check Catalog](artifact/references/harness-checks.md)
- [FTO Report Quality Assessment Template](artifact/assets/assessment-report-template.md)
- [PatSnap MCP Servers](https://open.patsnap.com/marketplace/mcp-servers)
- [PatSnap Patent Research](https://open.patsnap.com/marketplace/mcp-servers/patsnap-ip-searching)
- [Advanced Patent Search](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Global Core Patents](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, HTML]

**Output Format:** [Markdown guidance with optional JSON inputs, static HTML assessments, validation JSON, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce local assessment reports, normalized independent-search comparison outputs, and validation harness artifacts; optional patent-search connectors require user-configured access.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
