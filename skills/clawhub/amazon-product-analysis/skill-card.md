## Description:

Turn an Amazon product link into an evidence-based short-form video script by extracting listing selling points, mining buyer review language, and producing a shot-by-shot script after the user chooses a content direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and content creators use this skill to turn a specific Amazon product page into a concise content strategy brief and short-form video script grounded in listing facts and embedded buyer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill browses Amazon product pages and relies on public listing and embedded review text, which may be incomplete or affected by page access limits.

Mitigation: Use browser-rendered page access, disclose thin review coverage when it occurs, and avoid asking users to log in or access full review pages that hit account boundaries.

Risk: A broad trigger could route non-Amazon product requests into a workflow designed for Amazon listings.

Mitigation: Confirm that the input is a specific Amazon product page or short link before analysis, and tighten trigger routing in a future version.

Risk: Generated marketing copy could overstate unsupported product claims if script lines are not tied back to source evidence.

Mitigation: Keep each shot traceable to listing data or authentic embedded buyer language and avoid using unverified prices, unavailable video content, or inferred claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/amazon-product-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown brief and shot-by-shot script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend insights.md and script.md files for organizing the product brief and final script; does not generate video files.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
