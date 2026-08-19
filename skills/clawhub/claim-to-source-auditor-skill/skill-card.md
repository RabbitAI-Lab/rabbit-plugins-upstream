## Description:

Audits articles, reports, drafts, and series by extracting verifiable claims, tracing them to primary or reliable secondary sources, classifying support status and severity, and producing structured claim-to-source audit outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, researchers, and analysts use this skill to verify high-risk factual claims, citations, regulatory statements, financial figures, direct quotes, and cross-platform article versions before publication or revision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit CSVs and gold-set files may store claim text, verdicts, source summaries, links, and other sensitive draft or internal-log content.

Mitigation: Use the skill on sensitive material only when that storage is acceptable, and require a clear destination before saving audit or regression artifacts.

Risk: Published content may be changed if a user accepts revisions based on the audit.

Mitigation: Keep audit and editing steps separate, and require explicit user acceptance before applying revisions to published content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Structured Markdown reports and CSV audit files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audit-problems CSV rows, a source register, cross-platform comparison, regression check, and an optional gold-set CSV.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
