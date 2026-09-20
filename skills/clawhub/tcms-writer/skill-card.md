## Description:

For tech-product marketing teams, tcms-writer turns product knowledge bases, brand rules, and content briefs into 1500-3000 word brand-side drafts for technical blogs, customer case studies, and product write-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Technology product marketing teams use this skill to draft long-form brand marketing content from an approved brief, product knowledge base, brand rules, and article template. It is intended for promotional product-positioning drafts, not neutral industry research, short-form social content, channel adaptation, or automatic publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad writing requests that are not intended to be brand-side long-form marketing drafts.

Mitigation: Confirm the user has a content brief and that the requested article is a technical blog, customer case study, or product write-up before drafting.

Risk: Drafts could include unsupported data points, product claims, customer identifiers, or internal information if the source material is not reviewed carefully.

Mitigation: Use only approved knowledge-base or published sources, keep the generated source-trace table, apply the sensitive-term and customer anonymization rules, and review the draft before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-writer)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Brand and content rules](artifact/references/brand-rules.md)
- [Sensitive terms and prohibited expressions](artifact/references/sensitive-terms.md)
- [Technical blog template](artifact/references/templates/tech-blog.md)
- [Case study template](artifact/references/templates/case-study.md)
- [Product update template](artifact/references/templates/product-update.md)

## Skill Output:

**Output Type(s):** [markdown, text, guidance]

**Output Format:** [Markdown draft article plus Markdown source-trace table and pre-review checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a long-form draft and a companion review artifact; generated content requires human review before publication or channel adaptation.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
