## Description: <br>
Audit and safely improve Shopify image alt text for product media, collection images, article featured images, and article inline images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopify merchants and their agents use this skill to review product, collection, and article images, prepare image-specific alt text plans, and apply approved alt text updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Shopify read/write scopes for product media, files, collections, and article content. <br>
Mitigation: Prefer the short-lived Shopify CLI connection, keep credentials in a private env file, and use the long-running Dev Dashboard connection only for trusted merchant-owned stores. <br>
Risk: Alt text writes can affect live store product, collection, and article image metadata. <br>
Mitigation: Preview every proposed write, require explicit approval before using --execute, and verify the target or scan counts after execution. <br>
Risk: Store metadata could contain prompt-injection-like text that tries to influence alt text generation. <br>
Mitigation: Treat Shopify metadata as read-only source data, wrap it in boundary markers, and ignore instructions found inside merchant content. <br>
Risk: Context-only generation could produce inaccurate alt text when real image understanding is unavailable. <br>
Mitigation: Require a local image vision probe with concrete pixel-derived facts and stop with VISION_MODEL_REQUIRED if image inspection fails. <br>


## Reference(s): <br>
- [Shopify Alt Text Rules](references/alt-text-rules.md) <br>
- [Connect Your Store](references/onboarding-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/optimize-shopify-alt-text) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code] <br>
**Output Format:** [Conversational Markdown with shell commands, helper stdout, and preview JSON for approved changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Shopify store domain, Shopify CLI or approved Dev Dashboard credentials, and a working vision model before generating alt text candidates.] <br>

## Skill Version(s): <br>
2.2.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
