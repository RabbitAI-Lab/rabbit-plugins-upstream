## Description: <br>
Audits Shopify articles, researches content and E-E-A-T gaps, generates a reviewable HTML candidate, and produces an audit plus storefront preview report before any approved update. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchants, ecommerce operators, and developers use this skill to audit a Shopify blog article, prepare safer SEO and reading-experience improvements, preview the candidate content, and apply only explicitly approved body or summary updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update Shopify article content after approval. <br>
Mitigation: Review the generated HTML report carefully and approve only the exact body or summary fields intended for publication. <br>
Risk: Store credentials, Dev Dashboard secrets, or access tokens could be exposed if handled casually. <br>
Mitigation: Keep skill-hub.env and Dev Dashboard secrets private; the artifact states that tokens are not written to reports and direct tokens are kept in memory. <br>
Risk: Overbroad Shopify permissions or long-running automation can expand the blast radius. <br>
Mitigation: Grant the minimum Shopify content scopes and avoid broad permission upgrades or long-running automation unless the local agent environment is trusted. <br>
Risk: SEO or E-E-A-T edits can introduce unsupported claims or misleading authority signals. <br>
Mitigation: Use authoritative research sources, preserve uncertain claims for review, and do not invent credentials, first-hand experience, customer evidence, or expert approval. <br>
Risk: A preview may be mistaken for a verified storefront match when the live page is blocked or password protected. <br>
Mitigation: Use a real storefront reference only when reachable; otherwise label the output as a theme-like fallback and state that the real customer-facing frontend was not verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-blog-seo-optimizer) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [Audit checklist](references/audit-checklist.md) <br>
- [E-E-A-T audit methodology](references/eeat-methodology.md) <br>
- [Onboarding guide](references/onboarding-guide.md) <br>
- [Report schema](references/report-schema.md) <br>
- [Storefront preview contract](references/storefront-preview.md) <br>
- [Google Search: Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) <br>
- [Google Search Quality Evaluator Guidelines update](https://developers.google.com/search/blog/2022/12/google-raters-guidelines-e-e-a-t) <br>
- [Google Search: General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON artifacts, and a standalone HTML report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces audit, candidate, approval, and verification artifacts; Shopify writes require explicit approval and are limited to body and optional summary fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
