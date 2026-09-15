## Description:

Provides agents with read-only Tongdaxin financial data access through OOMOL's oo CLI connector after inspecting live action schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, read, and discover Tongdaxin market data, screening, news, announcement, and research tools through an OOMOL-connected Tongdaxin account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Do not let an agent run installer commands automatically; use a trusted package manager or versioned installer, verify checksums or signatures where available, and inspect downloaded scripts before execution.

Risk: Connector access depends on the user's OOMOL-connected Tongdaxin account and current connection scopes.

Mitigation: Limit normal use to the intended Tongdaxin account, inspect live connector schemas before payload construction, and reconnect only when authentication, scope, credential, or app readiness errors require it.

## Reference(s):

- [Tongdaxin MCP product page](https://vip.tdx.com.cn/site/app/pc-mall/main.html#/page_product_mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tongdaxin)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions include data and meta.executionId fields when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
