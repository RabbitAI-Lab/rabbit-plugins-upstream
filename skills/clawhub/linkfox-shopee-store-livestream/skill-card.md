## Description: <br>
Provides agent-facing scripts and guidance for managing authorized Shopee store livestream sessions, items, comments, images, and metrics through LinkFox's Shopee developer proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and developers use this skill to create and manage Shopee livestream sessions, products, comments, moderation actions, media uploads, and metrics for an already authorized store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Skill API reference](references/api.md) <br>
- [Shopee Open Platform Livestream API](https://open.shopee.com/documents/v2/v2.livestream.upload_image?module=125&type=1) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-livestream) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, JSON files] <br>
**Output Format:** [Markdown guidance with shell commands; script output is JSON or a short text summary with full JSON saved to a local file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a trusted LinkFox API key and authorized Shopee store tokens. Confirm store-mutating actions before running scripts, and monitor or clean generated response files because they may contain shop, customer-interaction, media, or metric data.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
