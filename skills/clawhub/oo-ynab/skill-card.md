## Description:

YNAB lets agents search and read YNAB account, plan, transaction, category, payee, month, settings, and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer YNAB questions by querying an OOMOL-connected YNAB account with the oo CLI. It supports read-oriented account, budget, category, month, payee, plan, settings, transaction, and user lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive financial data through an OOMOL-connected YNAB account.

Mitigation: Use it only when the user accepts OOMOL processing YNAB financial data and keep credentials managed through the connected account flow.

Risk: First-time setup documents remote installer one-liners for the oo CLI.

Mitigation: Prefer a pinned, signed, or package-manager installation path, or verify the installer source and integrity before running it.

Risk: Future connector versions may add actions that mutate or delete YNAB data.

Mitigation: Treat the current skill as read-only; require explicit user confirmation for any future write or destructive action and its exact payload.

## Reference(s):

- [YNAB homepage](https://www.ynab.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ynab)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions should fetch the live action schema before execution; responses include a data object and meta.executionId.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
