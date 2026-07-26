## Description: <br>
Discover restaurants with advanced filters, place single or group orders on Wolt.com after confirmation, reorder past favorites, track status in real time, contact support for delays, and send updates to Slack or other connected channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dviros](https://clawhub.ai/user/dviros) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to discover Wolt restaurants, build carts, place confirmed food orders, track deliveries, and coordinate group orders or delivery updates through connected channels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a logged-in Wolt browser session and access account, address, order, and payment-context information. <br>
Mitigation: Install only for trusted use and verify the active Wolt account, address, restaurant, cart, payment method, and total before approving checkout. <br>
Risk: The skill can place real orders and contact support after user approval. <br>
Mitigation: Require explicit confirmation before final checkout or support contact, and review the support message before it is sent. <br>
Risk: Order updates and tracking details may be sent to Slack or other connected channels. <br>
Mitigation: Use private or narrowly scoped channels and avoid sending order updates to broad or public destinations. <br>


## Reference(s): <br>
- [Wolt](https://wolt.com) <br>
- [Wolt Israel](https://wolt.com/il) <br>
- [ClawHub Skill Page](https://clawhub.ai/dviros/skills/wolt-orders) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown summaries, tables, confirmations, tracking updates, support relays, and channel notification messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires browser.enabled and explicit user confirmation before checkout or support contact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
