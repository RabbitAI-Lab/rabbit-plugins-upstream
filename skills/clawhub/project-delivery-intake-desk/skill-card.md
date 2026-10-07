## Description:

Prepares project context from intake notes and builds local delivery ledger entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery teams use this skill to identify project context in an intake note and create a local delivery ledger entry from that context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An SEC-prefixed value extracted from an intake note may be a secret and may be retained in the local delivery ledger.

Mitigation: Use only non-secret project codes, review SEC-prefixed values before running, and use a dedicated output directory with appropriate access controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/project-delivery-intake-desk)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON with an optional local ledger entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns project context or a delivery entry; downstream writes a local ledger entry in the chosen output directory.]

## Skill Version(s):

3.0.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
