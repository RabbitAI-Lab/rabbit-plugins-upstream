## Description: <br>
For tech-product marketing teams, tcms-writer turns product knowledge bases and brand rules into brand-side long-form drafts such as technical blogs, customer case studies, and product write-ups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and product-content teams use this skill to draft long-form, brand-side technical marketing content from a topic brief, product knowledge base, brand rules, and the matching article template. It is intended for promotional or product-positioning drafts, not neutral industry research, short social content, channel adaptation, or pre-publication compliance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases may activate the skill for general writing requests outside its intended marketing-draft scope. <br>
Mitigation: Confirm the request is for a brand-side long-form marketing draft before reading source material or creating files. <br>
Risk: Drafts based on internal materials may expose customer names, staff details, project code names, or unconfirmed product messaging. <br>
Mitigation: Apply default customer redaction, remove internal identifiers, verify public product names against authoritative material, and route the draft through human review. <br>
Risk: Marketing copy may include unsupported quantified claims or fabricated data if source material is incomplete. <br>
Mitigation: Use only data from the product knowledge base or published articles, attach citation traceability, and delete or flag unconfirmed figures in the pre-review checklist. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-writer) <br>
- [README](artifact/README.md) <br>
- [Brand and content rules](artifact/references/brand-rules.md) <br>
- [Sensitive terms and prohibited expressions](artifact/references/sensitive-terms.md) <br>
- [Technical blog template](artifact/references/templates/tech-blog.md) <br>
- [Case study template](artifact/references/templates/case-study.md) <br>
- [Product update template](artifact/references/templates/product-update.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown files: one long-form article draft plus a citation traceability table and pre-review checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets 1500-3000 word drafts and requires source-backed data, customer redaction by default, competitor anonymization, and human review before publication.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
