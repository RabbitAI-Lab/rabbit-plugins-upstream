## Description: <br>
RevenueCat metrics, customer data, and documentation search for subscription analytics, MRR, churn, customers, and RevenueCat docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeiting](https://clawhub.ai/user/jeiting) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to query RevenueCat project data, subscription metrics, customer records, and local RevenueCat API documentation from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose broad live administrative and financial actions through the RevenueCat API. <br>
Mitigation: Use the least-privileged or read-only RevenueCat key available and require manual confirmation before refund, cancellation, delete, webhook, entitlement, product, project, paywall, or virtual-currency changes. <br>
Risk: A RevenueCat API key may reveal sensitive project, customer, subscription, and revenue data. <br>
Mitigation: Store RC_API_KEY only in the runtime environment, avoid printing secrets, and review requested endpoints before execution. <br>
Risk: Large metrics or list queries can produce excessive output or incomplete analysis if ranges and pagination are not controlled. <br>
Mitigation: Use explicit date ranges, limits, and pagination guidance from the bundled API reference files. <br>


## Reference(s): <br>
- [RevenueCat ClawHub skill page](https://clawhub.ai/jeiting/skills/revenuecat) <br>
- [RevenueCat documentation](https://www.revenuecat.com/docs) <br>
- [RevenueCat documentation index for LLMs](https://www.revenuecat.com/docs/llms.txt) <br>
- [RevenueCat Developer API v2 Reference](references/api-v2.md) <br>
- [Customers API reference](references/customers.md) <br>
- [Subscriptions API reference](references/subscriptions.md) <br>
- [Metrics API reference](references/metrics.md) <br>
- [Rate limits reference](references/rate-limits.md) <br>
- [Error handling reference](references/error-handling.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, markdown, configuration] <br>
**Output Format:** [Markdown with inline shell commands and RevenueCat API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and the RC_API_KEY environment variable; API access is scoped by the provided RevenueCat key.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
