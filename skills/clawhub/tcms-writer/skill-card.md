## Description:

For tech-product marketing teams, tcms-writer turns a product knowledge base, brand rules, and a content brief into brand-side long-form drafts such as technical blogs, customer case studies, and product write-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and product teams use this skill to create 1500-3000 word brand-side drafts from a content brief, product knowledge base, and brand guidelines. It is intended for promotional or product-positioning long-form content, not neutral industry research, compliance review, social posts, short content, or channel adaptation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic writing requests such as draft or writing an article may activate the skill on sensitive product materials.

Mitigation: Confirm the intended article type, target product, source files, and confidentiality posture before using it with sensitive knowledge bases.

Risk: Drafts based on internal cases could expose customer names, unreleased product details, internal project names, or unsourced claims.

Mitigation: Apply the skill's default redaction rules, cite only sourced data, mark uncertain product capabilities for confirmation, and require human review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-writer)
- [README](artifact/README.md)
- [Brand and content rules](artifact/references/brand-rules.md)
- [Sensitive terms and prohibited expressions](artifact/references/sensitive-terms.md)
- [Case study template](artifact/references/templates/case-study.md)
- [Product update template](artifact/references/templates/product-update.md)
- [Tech blog template](artifact/references/templates/tech-blog.md)

## Skill Output:

**Output Type(s):** [markdown, files, guidance]

**Output Format:** [Markdown files: an article first draft plus a citation-traceability table and pre-review checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts target 1500-3000 words and require human review before publication or channel adaptation.]

## Skill Version(s):

1.2.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
