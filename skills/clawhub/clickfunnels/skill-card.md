## Description: <br>
ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to a ClickFunnels account through Maton, inspect business data, and prepare or execute approved sales, contact, order, course, form, and webhook operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent access or modify connected ClickFunnels business data, including contacts, products, orders, courses, forms, fulfillments, and webhooks. <br>
Mitigation: Review write actions before execution and confirm the target resource and intended effect, especially deletes, GDPR redaction, fulfillment changes, and webhook creation. <br>
Risk: The MATON_API_KEY grants access to the Maton proxy for the user's connected ClickFunnels account. <br>
Mitigation: Store MATON_API_KEY as an environment variable and avoid displaying, logging, or sharing the key in chat or command output. <br>
Risk: When multiple ClickFunnels connections exist, requests may affect the wrong account if no connection is specified. <br>
Mitigation: Use the Maton-Connection header when more than one active connection is available. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickfunnels) <br>
- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro) <br>
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference) <br>
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination) <br>
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering) <br>
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API endpoint references and Python, JavaScript, or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY environment variable, and an authorized ClickFunnels OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
