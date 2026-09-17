## Description:

Lokalise helps agents read, create, update, and delete Lokalise data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization operators use this skill to inspect Lokalise projects, keys, languages, and translations, and to make authorized changes to localization content. Destructive key deletion is available only with explicit review and approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute mutable code from OOMOL-hosted URLs.

Mitigation: Install the oo CLI only after independently trusting and verifying the installer source, and prefer pinned or otherwise auditable installation methods where available.

Risk: Lokalise write and destructive actions can change or delete translation data.

Mitigation: Inspect the live action schema, review the exact JSON payload and target resource, and get explicit approval before write or delete actions.

Risk: The skill uses OOMOL as the intermediary for Lokalise actions.

Mitigation: Install and use the skill only when that intermediary access model is acceptable for the user's Lokalise workspace and data governance requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lokalise)
- [Lokalise homepage](https://lokalise.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return JSON data and execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
