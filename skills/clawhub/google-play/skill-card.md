## Description:

Helps agents use the Google Play Developer API through a user's Maton connection to manage apps, products, subscriptions, purchases, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operators use this skill to inspect and manage Google Play apps, in-app products, subscriptions, purchases, and reviews through an authorized connection, with approval before changes or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to apps, purchases, subscriptions, or reviews can have customer-facing or financial effects.

Mitigation: Confirm each write, refund, cancellation, or review reply with the user before execution.

Risk: A new connection, hosted function, trigger, or destination can grant access or cause ongoing actions.

Mitigation: Obtain explicit approval for connections and review each deployment, trigger, and destination before enabling it.

Risk: Raw API keys may expose long-lived credentials.

Mitigation: Prefer the CLI's managed sign-in and avoid raw API keys unless the CLI cannot be used.

## Reference(s):

- [ClawHub Google Play skill](https://clawhub.ai/byungkyu/skills/google-play)
- [Maton](https://maton.ai)
- [Android Publisher API overview](https://developers.google.com/android-publisher)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses depend on the user's authorized Google Play connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
