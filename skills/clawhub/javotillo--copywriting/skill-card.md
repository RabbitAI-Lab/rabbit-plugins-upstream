## Description:

Helps agents write, rewrite, and improve persuasive website marketing copy for homepages, landing pages, pricing pages, feature pages, about pages, and product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javotillo](https://clawhub.ai/user/javotillo)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external marketing teams, founders, and developers use this skill to draft or improve website copy that clearly explains an offer, handles objections, and guides visitors toward a primary action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read existing product-marketing context files before drafting copy, so unrelated sensitive information stored in those files could be exposed in generated copy or reasoning.

Mitigation: Keep unrelated secrets out of `.agents/product-marketing.md`, `.claude/product-marketing.md`, and legacy product marketing context files; review generated copy before publication.

Risk: Generated marketing claims, proof points, testimonials, or statistics could be inaccurate if the user has not provided verified source material.

Mitigation: Require human review for factual claims and only publish proof points, customer quotes, or performance numbers that are backed by approved sources.

## Reference(s):

- [Copy Frameworks Reference](references/copy-frameworks.md)
- [Natural Transitions](references/natural-transitions.md)
- [Copywriting skill page](https://clawhub.ai/javotillo/skills/copywriting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with sectioned page copy, annotations, headline or CTA alternatives, and optional SEO metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include headlines, subheadlines, CTAs, section body copy, rationale, page titles, and meta descriptions when relevant.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
