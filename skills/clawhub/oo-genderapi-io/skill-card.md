## Description:

Operates GenderAPI.io through an OOMOL-connected account to infer likely gender from an email address, first name, or username.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run GenderAPI.io lookups through OOMOL, including lookup by email address, first name, or username. The skill is suited to read-only enrichment workflows where the user has already connected GenderAPI.io in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include mutable remote installer commands for the oo CLI, which can create supply-chain risk if run automatically or without verification.

Mitigation: Have a user review installation steps, use a verified and versioned package or documented manual install path with checksum or signature validation, and avoid letting an agent run remote installer commands automatically.

Risk: Submitted email addresses, names, or usernames may be processed by OOMOL and GenderAPI.io during lookup requests.

Mitigation: Confirm that the identifiers are appropriate to submit to connected third-party services before running the lookup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-genderapi-io)
- [GenderAPI.io homepage](https://www.genderapi.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include GenderAPI.io result data and OOMOL execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
