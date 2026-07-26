## Description: <br>
Audits and rewrites Shopping and Performance Max product feeds, including title and description patterns, required and recommended attributes, GTIN, availability, price hygiene, disapproval triage, and feed-driven asset or listing-group structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, ecommerce teams, and agent users use this skill to repair Shopping or Performance Max product-feed quality before or during paid campaigns. It produces feed remediation guidance for disapprovals, missing attributes, truthful title and description rewrites, price and availability mismatches, and feed-based campaign grouping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product-feed exports and Merchant Center diagnostics may contain sensitive commercial catalog, pricing, availability, and performance context. <br>
Mitigation: Use only exports the user is authorized to process, avoid storing raw catalogs, and confirm before saving remediation summaries to memory. <br>
Risk: Feed data, diagnostics, product descriptions, and landing-page content can contain untrusted instructions or misleading claims. <br>
Mitigation: Treat feed and page content as data, not instructions; verify claims, product identifiers, prices, availability, and policy-sensitive wording before use. <br>
Risk: Optional API-based feed pushes or catalog mutations could change live commerce data. <br>
Mitigation: Require explicit user approval before any feed push, catalog mutation, or API-driven change. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/product-feed-optimizer) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Feed Title Patterns](references/feed-title-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown remediation package with tables, rewritten feed fields, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write scoped summaries to memory/ad/product-feed-optimizer/ after user confirmation; does not store the full raw catalog.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
