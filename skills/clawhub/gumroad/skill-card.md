## Description: <br>
Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and storefront operators use this skill to query and manage Gumroad account data through Maton-managed OAuth, including product, sales, subscriber, license, offer code, variant, custom field, and webhook workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Maton API key and Maton-managed OAuth to access Gumroad account data. <br>
Mitigation: Install only if you trust Maton as the OAuth proxy and keep MATON_API_KEY private. <br>
Risk: The skill can perform write actions against Gumroad resources such as products, licenses, offer codes, variants, custom fields, connections, and webhooks. <br>
Mitigation: Confirm the target resource and intended effect before allowing any create, update, or delete request. <br>
Risk: When multiple Gumroad connections exist, requests may affect the wrong account if no connection is specified. <br>
Mitigation: Use the Maton-Connection header to select the intended Gumroad connection. <br>


## Reference(s): <br>
- [ClawHub Gumroad Skill](https://clawhub.ai/byungkyu/skills/gumroad) <br>
- [Gumroad API Overview](https://gumroad.com/api) <br>
- [Create API Application](https://help.gumroad.com/article/280-create-application-api) <br>
- [License Keys Help](https://help.gumroad.com/article/76-license-keys) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline HTTP examples and Python or JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and the MATON_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
