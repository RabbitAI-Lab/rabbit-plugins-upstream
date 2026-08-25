## Description:

This skill should be used when the user asks about their child's school arrival/dismissal through a SchoolPass parent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized users use this skill to read SchoolPass parent-account information such as students, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users must provide SchoolPass parent credentials to an npm-hosted MCP server.

Mitigation: Install only if comfortable with that credential flow, use a parent account, keep MCP configuration files private, and avoid shared machines.

Risk: Repeated rejected logins may trigger SchoolPass reCAPTCHA or account challenges.

Mitigation: Use the health check to distinguish reachability from authentication failures, and stop after a rejected login rather than retrying guessed credentials.

## Reference(s):

- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)
- [schoolpass-mcp source repository](https://github.com/chrischall/schoolpass-mcp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON configuration and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, parent-scoped SchoolPass account information; no password or session token should be echoed.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
