## Description:

Search and read Cloudflare Docs at developers.cloudflare.com through the OOMOL cloudflare_docs connector instead of calling Cloudflare APIs directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and read Cloudflare product documentation, including Workers, Pages, R2, D1, Zero Trust, DNS, CDN, AI products, and the Pages-to-Workers migration guide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded content directly into a shell.

Mitigation: Use the OOMOL CLI only after independently trusting and verifying the installer source; prefer signed packages, pinned releases, checksum or signature verification, or manual inspection before execution.

Risk: The skill depends on an OOMOL-connected Cloudflare Docs connector with credentials handled server-side.

Mitigation: Run connector actions only for documentation retrieval, reconnect only when an auth or connection error requires it, and confirm any future action tagged write or destructive before execution.

## Reference(s):

- [Cloudflare Docs](https://developers.cloudflare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-cloudflare-docs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
