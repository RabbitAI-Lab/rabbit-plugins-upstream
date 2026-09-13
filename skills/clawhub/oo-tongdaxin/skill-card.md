## Description:

Tongdaxin (vip.tdx.com.cn). Use this skill for ANY Tongdaxin request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Tongdaxin connector schemas and run read-only financial data, screening, news, announcement, and research queries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path instructs users to run a remote installer directly in a shell.

Mitigation: Review the installer before running it, and prefer a pinned, signed, or checksum-verifiable oo CLI release.

Risk: Connector calls depend on an OOMOL-connected account and live Tongdaxin action schemas.

Mitigation: Inspect the live action schema before constructing payloads and use the skill for read-only Tongdaxin data operations.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Tongdaxin Homepage](https://vip.tdx.com.cn/site/app/pc-mall/main.html#/page_product_mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for schema inspection and read-only connector calls; command responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
