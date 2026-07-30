## Description: <br>
Audit a Shopify Article, research content and E-E-A-T gaps, generate a reviewable HTML candidate, and produce one audit-plus-storefront-preview report before any approved update. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Merchants, content operators, and developers use this skill to audit Shopify blog articles, prepare evidence-aware SEO and reading-experience improvements, preview the proposed article HTML, and apply approved body or summary updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update Shopify article content after approval. <br>
Mitigation: Review the generated HTML report and exact proposed fields before using --execute; the helper requires an explicit approval marker and limits writes to body and optional summary. <br>
Risk: Shopify client secrets, access tokens, or automation tokens could expose store access if shared improperly. <br>
Mitigation: Keep credentials in the private env file, never paste them into chat or reports, and rely on the helper's in-memory token handling. <br>
Risk: SEO or E-E-A-T edits could introduce unsupported or misleading claims. <br>
Mitigation: Use the E-E-A-T methodology, preserve uncertain claims for review, require merchant-supplied evidence for credentials or first-hand experience, and do not invent authority signals. <br>
Risk: A generated storefront preview may not match the live theme when the public page is blocked or password protected. <br>
Mitigation: Label fallback previews clearly, state that the real storefront was not verified, and avoid claiming pixel-perfect theme fidelity. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/lvsao/skills/shopify-blog-seo-optimizer) <br>
- [Project homepage from ClawHub metadata](https://github.com/lvsao/shopify-skill-hub) <br>
- [Connect Your Store](references/onboarding-guide.md) <br>
- [Audit checklist](references/audit-checklist.md) <br>
- [E-E-A-T audit methodology](references/eeat-methodology.md) <br>
- [Audit, candidate, and approval artifact contract](references/report-schema.md) <br>
- [Storefront preview contract](references/storefront-preview.md) <br>
- [Google helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) <br>
- [Google Search Quality Evaluator Guidelines update](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t) <br>
- [Google structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON audit, candidate, approval-plan, and standalone HTML report artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Shopify store configuration; approved execution writes only Article body and optional summary fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
