## Description:

Faraday helps agents search and read Faraday account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to let an agent retrieve Faraday accounts, datasets, scopes, targets, traits, and usage information without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes one-line remote installer commands for the oo CLI, which could execute changing code on a user's machine.

Mitigation: Install the oo CLI only through a verified, pinned, or manually reviewed method, and do not allow an agent to run the installer automatically.

Risk: Authentication, connection, and billing steps can affect access to the user's OOMOL and Faraday accounts.

Mitigation: Require the user to confirm sign-in, account connection, and billing recovery steps before running them.

## Reference(s):

- [ClawHub Faraday Skill](https://clawhub.ai/oomol/skills/oo-faraday)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Faraday Homepage](https://faraday.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector action names, schema inspection commands, JSON payload examples, and Faraday read results.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
