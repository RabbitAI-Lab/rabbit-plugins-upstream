## Description:

Apify API integration with managed authentication for running web scrapers and actors and managing datasets, key-value stores, schedules, and related Apify resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to operate Apify through Maton-managed authentication, including reading account data, running actors, and managing storage, schedules, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Maton API key or provider credential could be exposed if printed, stored in files, passed on command lines, or committed.

Mitigation: Prefer OAuth, let the CLI and operating system credential store handle secrets, and avoid exposing MATON_API_KEY.

Risk: Write operations, deletions, actor runs, schedule changes, and webhook changes can modify an Apify account or spend credits.

Mitigation: Review the target connection and require explicit user approval before any actor run, deletion, schedule, webhook, or other write operation.

Risk: Schedules and webhooks can keep operating after the conversation ends.

Mitigation: Confirm persistence with the user before creation or modification, and review existing resources before changing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/apify-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Apify API Reference](https://docs.apify.com/api/v2)
- [Apify Actors Documentation](https://docs.apify.com/actors)
- [Apify Storage Documentation](https://docs.apify.com/storage)
- [Apify Schedules Documentation](https://docs.apify.com/schedules)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, API paths, JSON request bodies, and operational cautions.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
