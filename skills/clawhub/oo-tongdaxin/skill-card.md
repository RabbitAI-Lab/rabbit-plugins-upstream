## Description:

Tongdaxin enables agents to operate Tongdaxin through the OOMOL-connected oo CLI for market data retrieval, financial research, screening, and connector action execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market researchers use this skill to query Tongdaxin market data, company profiles, financial statements, news, reports, indicators, and screening results through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts directly in a shell.

Mitigation: Prefer the official install guide or inspect and verify the installer before running it.

Risk: The call_tool action is tagged destructive and may remove or overwrite data.

Mitigation: Confirm the exact target, payload, and effect with the user, and require explicit approval before execution.

Risk: The skill depends on an OOMOL account connection, Tongdaxin credentials, and account billing state.

Mitigation: Run login, connection, or billing setup only when a command fails for that specific reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tongdaxin)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Tongdaxin homepage](https://vip.tdx.com.cn/site/app/pc-mall/main.html#/page_product_mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo connector commands; destructive call_tool actions require explicit user approval.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
