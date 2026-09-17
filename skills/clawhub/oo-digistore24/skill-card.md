## Description:

Digistore24 helps agents search and read buyer, product, purchase, sales, and account information from a connected Digistore24 account through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Digistore24 account data through an OOMOL-connected account, including buyers, products, purchases, sales, and account-owner information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes first-time setup commands that execute remote installer scripts.

Mitigation: Run installer commands only when setup is required, after independently verifying the oo CLI installation source and understanding what it installs.

Risk: The skill can access buyer, purchase, sales, and account-owner data from a connected Digistore24 account.

Mitigation: Use the skill only for intended Digistore24 queries and handle returned account data as sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-digistore24)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Digistore24 homepage](https://www.digistore24.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated OOMOL oo CLI connection to Digistore24; connector responses may contain sensitive buyer, purchase, sales, and account-owner data.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
