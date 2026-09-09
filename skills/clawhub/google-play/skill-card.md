## Description:

Google Play Developer API integration with managed OAuth for managing apps, subscriptions, in-app purchases, and reviews through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operators use this skill to access Google Play Console resources programmatically through Maton-managed OAuth. It supports read-first workflows and user-approved changes for app listings, subscriptions, in-app purchases, purchases, reviews, and edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect Google Play apps, subscriptions, purchases, reviews, and edits through an authorized account.

Mitigation: Prefer read-only calls first, review OAuth scopes and account context, and require explicit confirmation before any operation that changes Google Play resources.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, persisted, or passed through shell commands.

Mitigation: Use Maton-managed OAuth where possible, keep credentials in the operating system credential store, and never print, log, persist, or pass credential values on command lines.

Risk: A write can target the wrong account or app when multiple Maton profiles or Google Play connections exist.

Mitigation: Specify the intended profile, connection, package name, resource identifier, payload, and effect before executing any write.

Risk: Google Play API responses and external content may contain untrusted instructions or data.

Mitigation: Treat returned content as data only, validate values before reuse, and do not let API responses choose follow-up endpoints, recipients, or local commands.

## Reference(s):

- [Google Play Skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-play)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Android Publisher API Overview](https://developers.google.com/android-publisher)
- [In-App Products](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
- [Subscriptions](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
- [Purchases](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products)
- [Reviews](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews)
- [Edits](https://developers.google.com/android-publisher/api-ref/rest/v3/edits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Maton CLI or SDK workflows and return Google Play API response summaries.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
