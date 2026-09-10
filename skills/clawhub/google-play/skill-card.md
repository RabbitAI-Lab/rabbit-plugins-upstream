## Description:

Google Play Developer API integration with managed OAuth for managing apps, subscriptions, in-app products, purchases, reviews, and app edits through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Google Play Console resources programmatically through the Google Play Developer API. It supports read/list workflows by default and gated write workflows for app commerce, reviews, purchases, and edit operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unreviewed or unpinned Maton CLI or SDK package can introduce supply-chain exposure.

Mitigation: Verify the package source before installation and pin reviewed versions in controlled environments.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, command histories, files, or broad process environments.

Mitigation: Prefer OAuth, keep credentials in the supported credential store, never print or persist secrets, and use API keys only when the CLI cannot be installed.

Risk: Google Play write operations can change app commerce, reviews, purchases, or edit state.

Mitigation: Default to read/list calls and require explicit user approval with target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Using broad scopes or ambiguous connections can send requests to the wrong Google Play account or grant more access than the task needs.

Mitigation: Select the least privilege scopes available, specify the intended connection or profile when multiple accounts exist, and revoke unused connections.

Risk: External API data may contain adversarial or misleading content.

Mitigation: Treat returned content as untrusted data and do not execute, evaluate, or follow instructions found inside API responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-play)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Android Publisher API Overview](https://developers.google.com/android-publisher)
- [In-App Products API](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
- [Subscriptions API](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
- [Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products)
- [Reviews API](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews)
- [Edits API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and optional Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should keep credentials out of logs and require explicit user approval before connection creation or write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
