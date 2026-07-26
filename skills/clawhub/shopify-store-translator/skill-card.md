## Description: <br>
Translate Shopify store resources into a target language with preview-first review, market checks, and approved writes. Use for direct API translation, outdated translation audits, or Shopify CSV translation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchants, ecommerce operators, and developers use this skill to prepare, review, and apply Shopify translations across store resources, locales, and markets. It supports direct Admin API translation workflows, outdated translation audits, and Shopify CSV translation preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopify write access can change translations, locales, and market web-presence settings beyond a simple translation review. <br>
Mitigation: Require an explicit preview before any write that lists the exact resources, locales, markets, web presences, and full alternateLocales lists that will change. <br>
Risk: Long-running credentials and the optional automation token increase unattended access risk. <br>
Mitigation: Use the quick browser connection by default, and enable long-running credentials or the automation token only when the merchant specifically needs unattended approved permission releases. <br>
Risk: Source text being translated may contain prompt-injection-like instructions. <br>
Mitigation: Treat source text strictly as read-only data, wrap translatable content in boundary markers, and translate any instruction-like content literally rather than following it. <br>


## Reference(s): <br>
- [Shopify Store Translator skill page](https://clawhub.ai/lvsao/skills/shopify-store-translator) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [Business Field Map](references/business-field-map.md) <br>
- [Market & Language Setup Reference](references/market-lang-setup.md) <br>
- [Connect Your Store](references/onboarding-guide.md) <br>
- [Translation API Reference](references/translation-api.md) <br>
- [Shopify TranslatableResourceType](https://shopify.dev/docs/api/admin-graphql/latest/enums/TranslatableResourceType) <br>
- [Shopify translatableResources query](https://shopify.dev/docs/api/admin-graphql/latest/queries/translatableresources) <br>
- [Shopify translationsRegister mutation](https://shopify.dev/docs/api/admin-graphql/latest/mutations/translationsRegister) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON and CSV review artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary user-facing artifact is translation-audit.csv; candidate and patch files may be JSON, and translated Shopify CSV output may be produced for CSV mode.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
