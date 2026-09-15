## Description:

Google Play Developer API (Android Publisher) integration with managed OAuth for managing apps, subscriptions, in-app purchases, purchases, reviews, and edits through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interact with Google Play Console programmatically through the Google Play Developer API. It supports routine reads and user-approved writes for app products, subscriptions, purchases, reviews, and transactional edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on a connected Google Play developer account, including writes that affect subscriptions, purchases, reviews, and edits.

Mitigation: Use OAuth when possible, grant the narrowest Google Play access available, default to read/list calls, and confirm the target resource, payload, and intended effect before every write.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment, which can leak through logs, shell history, child processes, or persisted files.

Mitigation: Use the Maton CLI credential store when available; if raw HTTP is necessary, keep the key in a secret-managed environment, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Hosted functions and triggers can turn approved Google Play actions into recurring automation.

Mitigation: Deploy only user-authored or user-reviewed functions, prefer DENY_ALL network policy, scope connections narrowly, and require separate approval for each function deploy, trigger, and destination.

Risk: Trigger destinations can create persistent forwarding of event payloads, including personal or business data from connected event sources.

Mitigation: Keep destinations on api.maton.ai or *.maton.app unless the user explicitly approves a named third-party host, forward only necessary fields, and do not place Maton or provider credentials in destination headers or body templates.

Risk: External API responses and trigger payloads may contain untrusted free text or sensitive identifiers such as purchase tokens, review text, email addresses, or private repository content.

Mitigation: Treat returned content as data, not instructions; avoid command interpolation or eval, redact sensitive identifiers in shared output, and avoid logging full payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-play)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Android Publisher API overview](https://developers.google.com/android-publisher)
- [In-App Products API](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)
- [Subscriptions API](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions)
- [Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products)
- [Reviews API](https://developers.google.com/android-publisher/api-ref/rest/v3/reviews)
- [Edits API](https://developers.google.com/android-publisher/api-ref/rest/v3/edits)
- [Time trigger reference](references/time/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated Maton CLI commands, raw HTTPS examples for constrained environments, hosted function examples, and trigger configuration guidance.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
