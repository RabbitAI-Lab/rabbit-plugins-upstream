## Description:

Audits articles, reports, drafts, or related versions by extracting verifiable claims, tracing them to primary or reliable secondary sources, classifying support status and severity, and producing structured fact-audit outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, researchers, and content teams use this skill to check factual claims, source support, cross-platform consistency, and regression against prior audits before or after publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle sensitive unpublished drafts, internal logs, or local evidence while producing audit outputs.

Mitigation: Use an approved output directory, limit input access to intended materials, and review generated reports and regression files before sharing.

Risk: Accepted revisions to published content could change source-sensitive facts, quotations, regulatory references, or citations.

Mitigation: Require human review before applying revisions and preserve annotations for citation, judgment, or regulatory-reference changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured Markdown report with CSV-style audit and optional regression records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes claim status, severity, evidence summary, required action, source register, and optional gold-set regression rows.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
