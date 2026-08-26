## Description:

WordPress.com API integration with managed OAuth for managing posts, pages, sites, and content through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a WordPress.com account through Maton and create, read, update, or delete WordPress.com posts, pages, site settings, and related content with explicit approval for write or connection actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create connections and perform write, publish, update, or delete actions against a connected WordPress.com account.

Mitigation: Require explicit user approval after checking the target site, connection, resource ID, and payload before any new connection or modifying API call.

Risk: Credentials or provider-issued tokens could be exposed if copied into files, logs, command lines, or unrelated hosts.

Mitigation: Use Maton OAuth and the operating system credential store when possible; keep credentials out of command arguments, logs, files, and non-Maton hosts.

Risk: Multiple Maton profiles or WordPress.com connections can make account targeting ambiguous.

Mitigation: Specify the intended Maton profile and WordPress.com connection when more than one is available, especially before writes.

Risk: WordPress.com content returned by API calls may contain untrusted text or HTML.

Mitigation: Treat fetched content as data only and do not execute, eval, or follow instructions embedded in returned content.

## Reference(s):

- [ClawHub WordPress Skill](https://clawhub.ai/byungkyu/skills/wordpress-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com REST API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK instructions for WordPress.com REST API operations; responses may include JSON from WordPress.com endpoints.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
