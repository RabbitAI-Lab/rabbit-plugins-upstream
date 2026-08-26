## Description:

Web access privileges for your agent. So your agent stops hitting walls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to consult operating profiles for external APIs before making calls, choosing safer endpoints, rate-limit posture, caching behavior, and authentication patterns. It helps agents avoid repeated failed requests and record observations for future access decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes guidance for authenticated third-party services and business-critical write surfaces such as Ghost, Stripe, GitHub, Notion, and Airtable.

Mitigation: Keep credentials in secure stores, avoid logging tokens or API keys, and require review before write actions to sensitive services.

Risk: API operating profiles can become stale as provider limits, endpoints, and policies change.

Mitigation: Treat profiles as operational guidance, check current provider responses and headers during use, and update observations when behavior changes.

Risk: The skill discloses local logging and cache behavior under the workspace data directory.

Mitigation: Review workspace log and cache retention expectations and avoid writing sensitive request contents into logs.

## Reference(s):

- [Service Profiles](references/profiles.md)
- [agent-tollbooth homepage](https://github.com/highnoonoffice/agent-tollbooth)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes service-specific API access notes, cache/log paths, and credential-handling cautions.]

## Skill Version(s):

2.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
