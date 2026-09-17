## Description:

Brex enables an agent to search and read Brex company, user, budget, expense, card account, and transaction data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Brex account records through an OOMOL-connected Brex account, including company, user, budget, expense, card account, and settled transaction data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive Brex financial records are routed through OOMOL.

Mitigation: Review organizational approval for OOMOL handling before installation and use the skill only for explicit, account-specific Brex read requests.

Risk: Inline installer commands pipe remote scripts into a shell.

Mitigation: Independently trust and verify the installer source before using those commands, or install the oo CLI through an approved internal process.

Risk: Broad Brex requests can expose more account data than intended.

Mitigation: Use the narrowest practical filters and inspect the live connector schema before running an action.

## Reference(s):

- [ClawHub Brex skill page](https://clawhub.ai/oomol/skills/oo-brex)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Brex homepage](https://www.brex.com/)
- [Brex icon](https://static.oomol.com/logo/third-party/brex.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before running read-only Brex actions.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
