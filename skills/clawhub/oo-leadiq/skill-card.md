## Description:

LeadIQ helps an agent search and read LeadIQ people, company, account, and credit data through an OOMOL-connected LeadIQ account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search LeadIQ for people and companies, enrich person records, and check account or credit balances from an OOMOL-connected LeadIQ account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute changing code on a user's machine.

Mitigation: Review the setup path before installing and prefer a manually verified or pinned oo CLI installation instead of allowing an agent to run pipe-to-shell or iex installer commands.

Risk: LeadIQ search inputs and returned data pass through OOMOL connector infrastructure.

Mitigation: Use the skill only when that data path is acceptable for the user's LeadIQ data handling requirements.

## Reference(s):

- [LeadIQ ClawHub skill page](https://clawhub.ai/oomol/skills/oo-leadiq)
- [LeadIQ homepage](https://leadiq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include LeadIQ result data and OOMOL connector execution identifiers.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
