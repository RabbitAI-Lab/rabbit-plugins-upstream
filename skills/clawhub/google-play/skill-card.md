## Description:

Google Play Developer API (Android Publisher) integration with managed OAuth for managing apps, subscriptions, in-app purchases, and reviews through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interact with Google Play Console programmatically through Maton-managed OAuth. It supports read and list workflows first, then carefully confirmed changes to app listings, subscriptions, in-app purchases, purchase actions, reviews, and app edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Play write operations can modify subscriptions, purchases, refunds, reviews, or app edits.

Mitigation: Default to read and list calls; require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, persisted, or passed through unsafe command lines.

Mitigation: Use Maton OAuth and the operating system credential store where possible; never print or persist credentials, and use the documented stdin-based fallback only when the CLI cannot be installed.

Risk: Requests may affect the wrong account when multiple Maton profiles or Google Play connections exist.

Mitigation: Specify the intended profile and connection for API calls, and verify active connections before performing changes.

Risk: Google Play API responses may contain untrusted external content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and validate values before using them in follow-up requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-play)
- [Maton](https://maton.ai)
- [Android Publisher API Overview](https://developers.google.com/android-publisher)
- [In-App Products API](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
- [Subscriptions API](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
- [Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products)
- [Reviews API](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews)
- [Edits API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Configuration guidance, Code, Markdown]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before new connections or write operations.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
