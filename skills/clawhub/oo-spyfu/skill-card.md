## Description:

SpyFu lets an agent query SpyFu through the OOMOL-connected oo CLI for domain, keyword, SEO, PPC, SERP, advertising history, and usage data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve account-backed SpyFu marketing intelligence through OOMOL, including domain competitor research, keyword metrics, rankings, top pages, ad history, and usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run unverified remote installer scripts on the user's machine.

Mitigation: Do not let an agent run the remote installer automatically; use an official, versioned install method with checksum or signature verification.

Risk: Account-backed SpyFu connector calls may consume connected service usage or credits.

Mitigation: Use the connector only when the user requests SpyFu data, and review usage or billing status when cost or quota matters.

## Reference(s):

- [ClawHub SpyFu skill page](https://clawhub.ai/oomol/skills/oo-spyfu)
- [SpyFu homepage](https://www.spyfu.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId; account-backed queries may consume connected service usage or credits.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
