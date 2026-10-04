## Description:

Guides developers in setting up and using Neon backend services, including Lakebase Postgres, branching, authentication, storage, functions, and the AI Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building apps or backends use this skill to choose Neon services, set up the CLI or MCP server, and work with database branches and related backend resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested setup or skill updates can install Neon tooling or alter the agent's installed skills.

Mitigation: Review installation and update commands before running them, especially for global installs.

Risk: Branch linking or checkout can write database connection strings or API credentials to local environment files.

Mitigation: Prefer OAuth or project-scoped access where possible; use --no-env-pull or runtime environment injection when secrets should not be written to disk.

## Reference(s):

- [ClawHub Neon skill release](https://clawhub.ai/andrelandgraf/skills/neon)
- [Neon CLI installation](https://neon.com/docs/cli/install.md)
- [Neon branching documentation](https://neon.com/docs/introduction/branching.md)
- [Authentication guidance](references/auth.md)
- [Claimable Neon guidance](references/claimable-neon.md)
- [Function trigger guidance](references/function-triggers.md)
- [Logs and Loki guidance](references/logs-loki.md)
- [Type-safe environment variable guidance](references/parse-env.md)
- [Neon SDK guidance](references/sdk.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest actions that install tooling or change remote Neon resources.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
