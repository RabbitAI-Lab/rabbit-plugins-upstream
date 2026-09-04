## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search queries to dLazy infrastructure and requires a dLazy API key.

Mitigation: Avoid sensitive search queries unless approved for the service, and use DLAZY_API_KEY for per-invocation credentials when persistent local login is not desired.

Risk: The dLazy CLI can store an API key in a local user configuration file.

Mitigation: Protect local configuration files and rotate or revoke organization API keys from the dLazy dashboard when access changes.

Risk: The artifact documents both --query in command help and --prompt in an example, which can confuse invocation.

Mitigation: Prefer --query for search_video requests and check `dlazy search_video -h` before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [JSON returned by the dLazy CLI, with command guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include stock video URLs and metadata; asynchronous use may return a generateId for polling.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
