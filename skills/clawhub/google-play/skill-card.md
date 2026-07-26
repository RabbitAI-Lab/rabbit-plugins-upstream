## Description: <br>
Google Play Developer API (Android Publisher) integration with managed OAuth for managing apps, subscriptions, in-app purchases, and reviews programmatically. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to access Google Play Console resources through Maton-managed OAuth, including app listings, in-app products, subscriptions, purchases, reviews, and edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires MATON_API_KEY for access to Google Play resources through Maton. <br>
Mitigation: Store MATON_API_KEY only in the environment or an approved secret store, avoid exposing it in prompts or logs, and rotate it if it is disclosed. <br>
Risk: Requests may affect the wrong Google Play connection when multiple accounts are available. <br>
Mitigation: Specify the intended Maton connection when more than one connection exists. <br>
Risk: Write actions can create, update, delete, refund, cancel, reply, or commit changes in Google Play resources. <br>
Mitigation: Use the least-privileged Google Play account or connection available and confirm the target resource and intended effect before each write action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-play) <br>
- [Publisher profile](https://clawhub.ai/user/byungkyu) <br>
- [Android Publisher API overview](https://developers.google.com/android-publisher) <br>
- [In-App Products API](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts) <br>
- [Subscriptions API](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions) <br>
- [Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products) <br>
- [Reviews API](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews) <br>
- [Edits API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with API paths and Python, JavaScript, JSON, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Google Play account through Maton.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
