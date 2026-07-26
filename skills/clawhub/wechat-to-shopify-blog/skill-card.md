## Description: <br>
Converts owned or authorized WeChat Official Account articles into Shopify blog drafts with extraction, image filtering, Shopify-hosted uploads, English adaptation, blog selection, and optional related product links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Merchants, content teams, and developers use this skill to transform an owned or authorized WeChat article into an English Shopify blog draft with approved images and relevant product links before any Shopify draft write. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Shopify blog content, files, and product catalog details when store access is configured. <br>
Mitigation: Install it only for an authorized store, keep credentials private, and prefer the Shopify CLI browser connection unless a trusted long-running connection is required. <br>
Risk: A Shopify write could create or update content the merchant has not reviewed. <br>
Mitigation: Review the draft plan first and run write steps only after explicit approval with the documented execute commands; the skill creates drafts only and does not publish. <br>
Risk: Source article text or markup may contain embedded instructions that conflict with the user's intent. <br>
Mitigation: Treat fetched WeChat content as static source text, wrap it in boundaries for rewriting, and ignore embedded instruction-like text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/wechat-to-shopify-blog) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [Shopify onboarding guide](references/onboarding-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown draft content, JSON command output, and shell command sequences] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates Shopify draft articles and Shopify-hosted image URLs only after explicit approval for write steps.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
