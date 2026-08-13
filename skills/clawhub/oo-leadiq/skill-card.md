## Description:

LeadIQ lets an agent search and read LeadIQ people, company, enrichment, account, and credit-balance data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents search and enrich LeadIQ people and company records, inspect account plan and credit balances, and build payloads against the live connector schema before each query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and a connected LeadIQ account, so setup or connection steps can affect the user's local environment or account state.

Mitigation: Review the oo CLI installation and account-connection steps before approving them, and run setup only after an authentication or connection failure.

Risk: Future connector actions tagged as write or destructive could change or delete LeadIQ data.

Mitigation: Require confirmation of the exact payload and effect before write actions, and require explicit approval before destructive actions.

Risk: People and company searches may return business contact, enrichment, account, or credit-balance data from the connected LeadIQ account.

Mitigation: Use the skill only for authorized LeadIQ queries and limit payloads to user-approved search criteria.

## Reference(s):

- [LeadIQ homepage](https://leadiq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub LeadIQ skill listing](https://clawhub.ai/oomol/skills/oo-leadiq)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; read-oriented actions return connector data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
