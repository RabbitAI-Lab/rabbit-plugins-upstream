## Description:

Use when creating English SEO blog content for Lanthome from a lanthomeskincare.com product URL, including Markdown articles, blog-editor HTML fragments, SEO metadata, internal links, and cover images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hwl1413520](https://clawhub.ai/user/hwl1413520)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content operators, and Lanthome-focused ecommerce teams use this skill to generate a complete editorial review package from a Lanthome product URL, including a long-form SEO article, CMS-ready HTML, SEO metadata, internal links, and a cover image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains under-scoped CMS editor automation guidance for writing and saving content inside a live UEESHOP editor.

Mitigation: Use the skill for local blog asset generation by default, and require explicit user authorization plus separate save and publish controls before any CMS editor injection is used.

Risk: Generated skincare content can become misleading if product, efficacy, certification, regulatory, or manufacturing claims are not supported by the source page.

Mitigation: Keep claims traceable to the product page, omit unclear facts, use conservative cosmetic language, cite authoritative sources for ingredient or regulation topics, and complete editorial review before publishing.

## Reference(s):

- [Lanthome SEO Blog Output Specification](artifact/references/output-spec.md)
- [Blog Fragment Template](artifact/assets/blog-fragment-template.html)
- [ClawHub Skill Page](https://clawhub.ai/hwl1413520/skills/seo-blog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance, Files]

**Output Format:** [Markdown article, editor-ready HTML fragment, PNG cover image, SEO metadata, internal links, and validation summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a unique slug-based output directory containing the article Markdown, blog-editor HTML fragment, and landscape cover PNG.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
