## Description: <br>
Uploads Shopee store images and videos through LinkFox's Shopee Media module wrapper for the six Shopee v2 media endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and e-commerce operators use this skill to upload Shopee store images and videos, including chunked video uploads, through LinkFox-authenticated Shopee Media API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopee shop, token-related, media request, or media response data may be stored in local LinkFox JSON records after calls. <br>
Mitigation: Use the skill only in workspaces where generated linkfox data will not be committed, and delete saved session folders when they contain sensitive account or media data. <br>
Risk: Shopee shop and media data is sent through LinkFox gateway endpoints to perform the advertised uploads. <br>
Mitigation: Install and run the skill only when routing this data through LinkFox is acceptable for the account, shop, and media involved. <br>


## Reference(s): <br>
- [Skill API Reference](references/api.md) <br>
- [Shopee Open Platform v2.media.upload_image](https://open.shopee.com/documents/v2/v2.media.upload_image?module=130&type=1) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON files with stdout JSON or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved locally under linkfox session data; small responses and --inline mode print full JSON, while larger responses print a summary.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
