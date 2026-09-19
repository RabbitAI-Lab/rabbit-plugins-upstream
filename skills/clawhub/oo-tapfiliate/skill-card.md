## Description:

Helps agents read, create, and update Tapfiliate data through OOMOL's Tapfiliate connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Tapfiliate affiliates, affiliate groups, clicks, conversions, commissions, and programs from an agent session. It is intended for schema-first Tapfiliate operations where read actions can run directly and write actions require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tapfiliate operations are routed through OOMOL with connected account access.

Mitigation: Use this skill only when the user is comfortable granting OOMOL the requested Tapfiliate access and routing Tapfiliate operations through that service.

Risk: Setup instructions include remote installer commands that can execute downloaded code.

Mitigation: Do not run curl-to-bash or PowerShell iex installer commands automatically; prefer an official package manager or a downloaded installer whose source, version, and integrity can be verified first.

Risk: Write actions can create or change Tapfiliate affiliates, groups, clicks, and conversions.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub Tapfiliate skill page](https://clawhub.ai/oomol/skills/oo-tapfiliate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Tapfiliate homepage](https://tapfiliate.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
