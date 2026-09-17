## Description:

Tongdaxin (vip.tdx.com.cn) lets an agent search and read Tongdaxin financial data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover available Tongdaxin market-data, screening, news, announcement, and research tools, then run read-only financial-data requests through OOMOL's connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands whose delivery is not verified by the skill.

Mitigation: Review safer installation or verification options before running the curl-to-bash or PowerShell iex commands.

Risk: Connector access depends on an OOMOL-connected Tongdaxin account and server-side credential injection.

Mitigation: Use the skill's setup and recovery steps only when authentication, connection scope, credential expiry, or billing errors occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tongdaxin)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Tongdaxin MCP product page](https://vip.tdx.com.cn/site/app/pc-mall/main.html#/page_product_mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
