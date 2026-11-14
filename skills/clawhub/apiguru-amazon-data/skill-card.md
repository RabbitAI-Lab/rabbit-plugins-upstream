## Description:

Live Amazon marketplace data from Apiguru (a paid third-party API, 3 free calls a day) - product details, prices, reviews, keyword search, best-sellers, deals, offers and stock, seller profiles, across 23 Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to answer user requests for current Amazon product, pricing, review, search, deals, stock, and seller information across supported marketplaces. It is intended for Amazon-specific data requests, not general shopping advice or other stores.

### Deployment Geography for Use:

Global (23 supported Amazon marketplaces)

## Known Risks and Mitigations:

Risk: The security scan was partial because some references in the skill description did not match bundled artifacts, so the available review evidence is incomplete.

Mitigation: Review the unresolved referenced materials before relying on the skill.

Risk: Some API calls can incur charges after the free allowance is used.

Mitigation: Ask the user before the first billable call or a batch or broad search, state the planned calls and cost, and stop at the agreed spending cap.

## Reference(s):

- [API endpoint reference](artifact/references/endpoints.md)
- [Costs and billing guidance](artifact/references/errors-and-costs.md)
- [Apiguru API user documentation](https://agent.apiguru.app/llms-full.txt)
- [Project homepage (listed in skill metadata)](https://github.com/apiguru-app/agent-kit)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [Structured JSON data with human-readable status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results vary by marketplace and query. A billable call requires user consent.]

## Skill Version(s):

1.1.62 (source: server release evidence and script version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
