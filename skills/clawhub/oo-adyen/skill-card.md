## Description:

Use this skill for Adyen search and read requests through an OOMOL-connected account instead of calling the Adyen API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Adyen connector schemas and retrieve accessible API credential, company, and merchant account information through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review and verify the oo CLI installer source before use, or prefer a pinned, signed, or package-manager installation path.

Risk: The connector can read Adyen credential, company, and merchant account information available to the connected OOMOL account.

Mitigation: Confirm the connected account scopes and expected readable data before running actions against production Adyen accounts.

Risk: Action inputs may become stale if constructed without the current connector contract.

Mitigation: Inspect the live action schema with oo connector schema before building each request payload.

## Reference(s):

- [ClawHub Adyen skill page](https://clawhub.ai/oomol/skills/oo-adyen)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Adyen homepage](https://www.adyen.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include live connector schemas, action payload guidance, and read-only Adyen account data returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
