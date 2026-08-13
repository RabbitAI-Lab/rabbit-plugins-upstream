## Description:

Audits articles, reports, drafts, or article series by extracting verifiable claims, tracing them to primary or reliable secondary sources, classifying support status, and producing structured claim-audit outputs with severity levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, researchers, and publication teams use this skill to verify high-risk factual claims, source support, quotes, regulatory statements, citations, and cross-platform consistency before or after publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect confidential drafts, research databases, or internal operational logs during claim audits.

Mitigation: Provide only materials approved for review and redact sensitive data when full source context is not required.

Risk: The skill may search external sources while verifying claims.

Mitigation: Avoid submitting private or embargoed claim details to external search channels unless that disclosure is approved.

Risk: The workflow can save audit CSVs and optional regression gold-set records.

Mitigation: Store generated audit files according to the publication team's data retention and access-control requirements.

Risk: Article text may be revised if the user explicitly accepts changes.

Mitigation: Keep revision review separate from the audit report and require editorial approval before publication.

## Reference(s):

- [Claim-to-Source Auditor Skill Page](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill)
- [Publisher Profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [text, markdown, CSV, guidance]

**Output Format:** [Structured Markdown audit report with optional CSV claim and gold-set records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces claim statuses, severity labels, source registers, cross-platform comparison notes, and revision guidance when requested.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
