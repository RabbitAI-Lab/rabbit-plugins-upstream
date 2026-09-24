## Description:

Google Play Developer API integration with managed OAuth for managing apps, subscriptions, in-app purchases, reviews, app edits, and related Google Play Console workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Google Play Developer API resources through Maton-authenticated commands and API calls. It is suited for account-authorized Google Play Console tasks such as listing products, managing subscriptions, handling purchases, replying to reviews, and creating approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide access to a user's Google Play account and workflows that may change subscriptions, purchases, reviews, or app edits.

Mitigation: Install and use it only for intended Google Play access, default to read and list operations, and require explicit user confirmation before any write or new connection.

Risk: Hosted functions, triggers, or destinations can create ongoing automation after the initial task.

Mitigation: Review each requested function deployment, trigger, and destination before creation, keep network access least-privilege, and delete automation that is no longer needed.

Risk: Raw responses and long-lived API keys can expose account or business data if copied into logs, files, environment variables, or third-party destinations.

Mitigation: Prefer OAuth, keep credentials in the Maton-supported credential store, avoid dumping full responses, and route data only to approved destinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-play)
- [Maton Homepage](https://maton.ai)
- [Android Publisher API Overview](https://developers.google.com/android-publisher)
- [In-App Products API](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
- [Subscriptions API](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
- [Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products)
- [Reviews API](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews)
- [Edits API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code examples, JSON examples, and API path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-approved Maton authentication and confirmation for writes, connection changes, function deployment, trigger creation, and destinations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
