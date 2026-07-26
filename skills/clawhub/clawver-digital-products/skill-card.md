## Description: <br>
Create and sell digital products on Clawver, including file uploads, pricing, published listings, and download tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External sellers and store operators use this skill to create, publish, update, archive, and monitor downloadable products on Clawver Marketplace. It is suited for digital goods such as art packs, ebooks, templates, software, and other downloadable content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API examples can create, publish, update, pause, or archive live product listings. <br>
Mitigation: Review product IDs, prices, uploaded file details, listing status changes, and archive/delete commands before execution. <br>
Risk: The skill uses CLAW_API_KEY to authorize store-management API calls. <br>
Mitigation: Use a scoped or revocable API key when available and keep the key in the environment rather than in prompts, files, or command history. <br>
Risk: Generated signed download URLs can grant access to customer digital files. <br>
Mitigation: Treat signed URLs as secrets and send them only to the intended customer over trusted channels. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nwang783/skills/clawver-digital-products) <br>
- [Clawver Store](https://clawver.store) <br>
- [Digital Products API Examples](references/api-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash curl commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY; generated API commands can change live product listings and should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
