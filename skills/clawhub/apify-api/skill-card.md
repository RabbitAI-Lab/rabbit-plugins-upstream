## Description:

Connects an agent to Apify through Maton to run actors and manage datasets, storage, schedules, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Apify users can ask an agent to run web scraping actors, retrieve datasets, manage storage, and configure schedules or webhooks through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Actor runs can consume Apify credits.

Mitigation: Confirm the actor and inputs with the user before starting a run.

Risk: Write and delete actions can change or remove account resources.

Mitigation: Default to read and list calls; confirm the target, payload, and effect before any change.

Risk: Schedules, webhooks, hosted functions, and triggers can keep running or forward data after the conversation.

Mitigation: Review the destination and lasting effects, and obtain explicit approval before creating or changing automation.

Risk: Connection access and raw API keys can expose account data if mishandled.

Mitigation: Use the approved Maton connection, prefer device login, and do not print, store, or send credentials to other hosts.

## Reference(s):

- [Apify skill release on ClawHub](https://clawhub.ai/byungkyu/skills/apify-api)
- [Maton homepage](https://maton.ai)
- [Apify API Reference](https://docs.apify.com/api/v2)
- [Maton Docs](https://docs.maton.ai)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the user's authorized Maton connection to Apify.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
