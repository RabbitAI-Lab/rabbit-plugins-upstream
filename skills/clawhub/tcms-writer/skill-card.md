## Description:

Tcms Writer helps tech-product marketing teams turn a product knowledge base, brand guidelines, and a content brief into brand-side long-form drafts such as technical blogs, customer cases, and product write-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing writers and product teams use this skill to draft 1500-3000 word brand-side technical articles from a clear content brief and source knowledge base. It is intended for long-form first drafts and review packages, not social posts, neutral industry research, or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A draft could expose internal customer names, staff names, project code names, or unapproved customer case details.

Mitigation: The skill defaults internal customer cases to redacted descriptions and requires human review before further use.

Risk: A draft could include unsupported numbers, product claims, or externally unconfirmed messaging.

Mitigation: The skill requires all data to come from the knowledge base or published articles, attaches citation traceability, and flags uncertain public-status claims for review.

Risk: The skill could be invoked too broadly in workspaces with many writing skills or sensitive product documents.

Mitigation: Narrow activation phrases for the workspace and provide a clear brief before use.

Risk: A first draft could be mistaken for publish-ready content.

Mitigation: The skill produces a draft and review package only; it does not publish or adapt content for channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-writer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Markdown files: a long-form article draft plus a citation-traceability table and pre-review checklist.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets 1500-3000 word drafts, records cited data points, and stops before publication or channel adaptation.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
