## Description: <br>
When the user wants to add, fix, or optimize schema markup and structured data on their site. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and SEO practitioners use this skill to create, fix, and debug schema.org structured data for web pages. It focuses on JSON-LD markup for common rich-result targets such as Organization, Product, FAQPage, Article, BreadcrumbList, and related page types. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated schema can be inaccurate if it describes content that is not visible on the target page. <br>
Mitigation: Review JSON-LD against the visible page content and remove unsupported properties before deployment. <br>
Risk: Structured data may be syntactically valid but still ineligible for rich results because required properties, nesting, or search-engine guidelines are not satisfied. <br>
Mitigation: Validate with the Google Rich Results Test and Schema.org Validator, then monitor Search Console structured-data reports. <br>
Risk: The skill may read local product-marketing context files when present to tailor recommendations. <br>
Mitigation: Review any local marketing context used by the agent and verify that generated markup does not expose private or outdated claims. <br>


## Reference(s): <br>
- [Schema Markup Examples](references/schema-examples.md) <br>
- [Schema.org](https://schema.org) <br>
- [Google Rich Results Test](https://search.google.com/test/rich-results) <br>
- [Schema.org Validator](https://validator.schema.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with JSON-LD code blocks and validation checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include implementation recommendations, task-specific questions, and structured-data testing steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; skill frontmatter metadata reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
