## Description:

Enables an agent to operate Coupang seller workflows through the OOMOL oo CLI connector for reading and updating products, orders, inventory, returns, prices, and quantities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and support agents use this skill to inspect Coupang seller products, orders, inventory, return requests, and to prepare user-confirmed updates to prices or quantities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts.

Mitigation: Use an already installed oo CLI when available; review and independently trust OOMOL installer sources before running the documented shell or PowerShell installer commands.

Risk: Write actions can change Coupang order, pricing, or inventory state.

Mitigation: Confirm the exact action, target identifiers, payload, and expected effect with the user before running any state-changing connector action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-coupang)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Coupang Homepage](https://www.coupang.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when run with the documented --json flag.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
