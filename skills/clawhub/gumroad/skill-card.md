## Description:

Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, storefront operators, and developers use this skill to query Gumroad account data and perform approved storefront operations such as license checks, product updates, offer-code management, sales review, and webhook setup through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Gumroad accounts can expose storefront data such as sales, customer records, subscribers, licenses, products, discounts, and webhooks.

Mitigation: Use OAuth, select the least-privileged account or scope available, verify the active Maton profile and Gumroad connection, and default to read or list calls before taking action.

Risk: Write operations can modify Gumroad products, licenses, offer codes, variants, custom fields, or webhooks.

Mitigation: Require explicit user approval before any POST, PUT, PATCH, or DELETE request, including the target resource, payload, and intended effect.

Risk: Long-lived Maton API keys or provider-issued tokens can leak if printed, stored, passed on command lines, or sent to the wrong host.

Mitigation: Prefer OAuth and CLI-managed credential storage; do not inspect, print, or persist credentials; send fallback API-key requests only to api.maton.ai.

Risk: Gumroad API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands or prompts, and keep local execution out of scope.

## Reference(s):

- [Gumroad API Overview](https://gumroad.com/api)
- [Gumroad License Keys Help](https://help.gumroad.com/article/76-license-keys)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Gumroad Skill](https://clawhub.ai/byungkyu/skills/gumroad)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Gumroad API paths, Maton CLI commands, OAuth and connection steps, and user-confirmation prompts for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
