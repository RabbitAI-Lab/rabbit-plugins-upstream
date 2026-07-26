## Description: <br>
Huo15 Marketingforce Website helps agents administer MarketingForce/T云 website content through CMS APIs, including articles, products, media, inquiries, SEO, analytics, settings, plugins, multilingual content, AI tools, and system operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Website administrators and authorized operators use this skill to review and modify MarketingForce/T云 CMS content, site settings, SEO data, forms, media, analytics, and related website operations through the included CLI and API reference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live browser session tokens can grant broad access to MarketingForce website administration. <br>
Mitigation: Install only for trusted, authorized operators; treat MF_X_TOKEN and MF_ADMIN_TOKEN like passwords, prefer short-lived or revocable tokens, and do not commit scripts/.env. <br>
Risk: CMS write, publish, and delete actions can change or remove public website content. <br>
Mitigation: Confirm every write, publish, and delete action; back up content before editing; preview drafts before publishing; prefer hiding content over deletion when possible. <br>
Risk: Inquiry and member commands can expose customer or user data in agent chat and logs. <br>
Mitigation: Run those commands only when customer-data exposure is acceptable and limit unnecessary disclosure in prompts, outputs, and logs. <br>


## Reference(s): <br>
- [MarketingForce T云 API Reference](references/reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-marketingforce-website) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown and command-line text with API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses operator-provided MarketingForce session tokens and can perform live CMS read, write, publish, and delete operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
