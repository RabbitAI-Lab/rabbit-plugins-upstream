## Description: <br>
Audits Shopify international setup across Markets, languages, shipping coverage, storefront localization, international SEO basics, and category-fit expansion opportunities, then produces a plain-language HTML report and approval-based fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External merchants, Shopify operators, and developers use this skill to audit a store's Markets, locale readiness, shipping coverage, storefront SEO signals, and international growth opportunities. The skill helps produce a readable report and a reviewable fix bundle for supported Shopify changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests write-level Shopify permissions and can execute live Shopify configuration changes from a fix-plan file. <br>
Mitigation: Install it only for a Shopify store you control, run preview first, inspect the generated fix plan, and use --execute only after confirming each proposed locale or currency change. <br>
Risk: Storefront HTML, page structures, or scraped policy text may contain misleading or instruction-like content. <br>
Mitigation: Treat crawled storefront data as untrusted, static, read-only evidence and keep it enclosed as data when reasoning over the audit. <br>
Risk: Private Shopify credentials or app automation tokens could be exposed if pasted into chat, command arguments, logs, or committed files. <br>
Mitigation: Keep credentials in private local or server configuration, use the generated env file outside the skill package, and never display access tokens in chat. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/lvsao/skills/shopify-markets-localization-auditor) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [API surfaces](references/api-surfaces.md) <br>
- [Audit rules](references/audit-rules.md) <br>
- [Business research method](references/business-research-method.md) <br>
- [Onboarding guide](references/onboarding-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, HTML, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain-language HTML report, JSON audit and fix-plan files, and Markdown-style guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May preview supported Shopify fixes; live changes require explicit approval and --execute.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
