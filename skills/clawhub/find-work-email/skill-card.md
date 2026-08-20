## Description:

Finds a verified work email address from a person's name and company domain, powered by Cargo providers prospeo and FullEnrich.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, growth, and operations users use this skill to look up work email addresses for named contacts at known company domains. It is intended for verified lookup workflows where unresolved rows should remain empty rather than guessed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends names and company domains to Cargo and provider services for work-email lookup.

Mitigation: Use it only for contacts and domains that are appropriate for Cargo and its providers to process.

Risk: The skill installs a global Cargo CLI and may persist Cargo credentials.

Mitigation: Review the CLI installation and authentication path before use, and use an account or token intended for this workflow.

Risk: The skill sends a Cargo session attribution record.

Mitigation: Review the attribution behavior before running the setup commands in environments where session metadata should not be shared.

Risk: The skill includes an unrelated prompt to star the publisher's GitHub repository using the user's GitHub account.

Mitigation: Decline the prompt unless the user explicitly wants that public account action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-work-email)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash command examples and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces provider lookup guidance and CLI commands; successful runs return work email results through Cargo providers, while unresolved rows remain empty.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
