## Description:

Helps agents retrieve Enormail account, contact, mailing list, sender, and mailing statistics through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Enormail users and support teams use this skill to look up contacts, mailing lists, mailings, senders, and delivery statistics through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup proposes running an unverified remote CLI installer.

Mitigation: Review the installer and prefer an official, manually verified installation before executing it.

Risk: A connected account can expose contact details, lists, senders, and mailing statistics.

Mitigation: Connect only an account whose Enormail data the agent is authorized to read, and limit sharing of retrieved results.

## Reference(s):

- [Enormail](https://enormail.eu)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Enormail skill on ClawHub](https://clawhub.ai/oomol/skills/oo-enormail)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown summaries of Enormail records and statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only account data; results depend on the connected account's access.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
