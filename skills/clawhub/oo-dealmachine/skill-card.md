## Description:

Provides DealMachine property search, property lookup, account details, field and filter discovery, and credit-cost estimation through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read DealMachine property data, inspect account and schema details, and estimate search credits through an OOMOL-connected DealMachine account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer an official, inspectable, versioned oo CLI installer with checksum or signature verification before running DealMachine actions.

Risk: DealMachine access is routed through OOMOL using server-side credentials.

Mitigation: Install only if OOMOL is an acceptable intermediary and connect only the DealMachine account intended for this skill.

## Reference(s):

- [DealMachine homepage](https://dealmachine.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub DealMachine skill page](https://clawhub.ai/oomol/skills/oo-dealmachine)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DealMachine account, property, field, filter, count, and credit-estimate results returned by the connector.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
