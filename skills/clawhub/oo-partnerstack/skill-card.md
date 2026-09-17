## Description:

PartnerStack helps agents read, create, and update PartnerStack data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve PartnerStack customers, partnerships, deals, leads, and create customers through an OOMOL-connected PartnerStack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer snippets that could be unsafe if an agent runs them automatically.

Mitigation: Install the oo CLI manually from a trusted source with verification, then use the skill for PartnerStack actions.

Risk: Customer creation changes PartnerStack state and can create incorrect records if the payload is wrong.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-partnerstack)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [PartnerStack homepage](https://partnerstack.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; customer creation requires user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
