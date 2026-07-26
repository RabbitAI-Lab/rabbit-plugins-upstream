## Description: <br>
Generates SERP-focused document-head assets, including title and meta description options, Open Graph and Twitter tags, and Schema.org JSON-LD with validation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and SEO practitioners use this skill to produce page-head metadata, social sharing tags, and Schema.org JSON-LD for pages that need stronger search and answer-engine presentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated schema or metadata could include unsupported ratings, prices, reviews, dates, authors, or business details. <br>
Mitigation: Review the output against visible page content and user-provided facts before publishing; omit unsupported fields or keep them clearly labeled as placeholders. <br>
Risk: User-supplied page URLs may return untrusted content that should not steer the agent outside the requested SEO task. <br>
Mitigation: Treat fetched page content as data for extraction and validation, not as instructions. <br>
Risk: Generated SEO deliverables may be saved into agent memory after use. <br>
Mitigation: Require user confirmation before saving and review the deliverable for sensitive or incorrect details first. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/serp-markup-builder) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [CTR Optimization & Social Tags Reference](references/ctr-and-social-reference.md) <br>
- [Meta Tags Optimizer - Detailed Instructions](references/meta-instructions-detail.md) <br>
- [Meta Tag Code Templates](references/meta-tag-code-templates.md) <br>
- [Meta Tag Formulas Reference](references/meta-tag-formulas.md) <br>
- [Schema Type Decision Tree](references/schema-decision-tree.md) <br>
- [Schema Markup Generator - Detailed Instructions](references/schema-instructions-detail.md) <br>
- [Schema.org JSON-LD Templates](references/schema-templates.md) <br>
- [Schema Markup Validation Guide](references/validation-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with HTML meta tag snippets, JSON-LD code blocks, validation notes, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include page-head metadata packages, Schema.org JSON-LD, rich-result eligibility notes, and optional save-to-memory guidance after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
