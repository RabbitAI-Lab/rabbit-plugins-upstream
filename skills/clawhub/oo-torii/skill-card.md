## Description:

Torii helps agents search and read Torii data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to retrieve Torii apps, contracts, users, organization details, transactions, and workflows through an OOMOL-connected Torii account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Use a verified, version-pinned installation path and avoid pipe-to-shell installers as written.

Risk: The generic connector action runner is broader than the read-only description.

Mitigation: Treat the skill as suitable for read-only Torii lookups unless a reviewer explicitly approves any state-changing connector action and payload.

Risk: The skill can access organization Torii data through OOMOL-managed credentials.

Mitigation: Install only when the user trusts OOMOL and the Torii connector with the organization's Torii data.

## Reference(s):

- [ClawHub Torii Skill](https://clawhub.ai/oomol/skills/oo-torii)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Torii Homepage](https://www.toriihq.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before action execution; command responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: skill metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
