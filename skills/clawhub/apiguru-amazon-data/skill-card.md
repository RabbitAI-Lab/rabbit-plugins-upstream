## Description:

Helps agents retrieve live product, price, review, offer, stock, seller, and search data from Apiguru for supported Amazon marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use this skill to answer requests for live Amazon product and seller data across 20 supported marketplaces, including price, stock, and review monitoring. It is not intended for other stores or general shopping advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyed requests may charge the user's Apiguru account.

Mitigation: Prefer keyless calls; obtain consent and agree on a spending cap before any billable request.

Risk: API credentials could be exposed if shared in commands or logs.

Mitigation: Accept keys only through the documented prompt, stdin, or user-specified file options; never echo them.

Risk: Feedback submissions are public and may disclose personal or sensitive information.

Mitigation: Review feedback text and contact details before submitting; omit sensitive information.

## Reference(s):

- [Apiguru project homepage (skill metadata)](https://github.com/apiguru-app/agent-kit)
- [Endpoint and marketplace reference](references/endpoints.md)
- [Costs, billing, and retries](references/errors-and-costs.md)
- [Apiguru agent API guide](https://agent.apiguru.app/llms.txt)

## Skill Output:

**Output Type(s):** [JSON data, Guidance, Shell commands]

**Output Format:** [JSON API responses and Markdown guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live marketplace data; keyless usage is quota-limited, and keyed calls may be billed.]

## Skill Version(s):

1.1.36 (source: ClawHub release metadata, scripts/probe.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
