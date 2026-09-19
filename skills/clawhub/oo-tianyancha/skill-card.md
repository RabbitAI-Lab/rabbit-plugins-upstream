## Description:

Tianyancha enables agents to search and read Tianyancha company intelligence through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve company search results, registration records, contact data, shareholder and investment details, risk records, judicial information, intellectual property data, news, and tender or bid notices from Tianyancha.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts directly with shell interpreters.

Mitigation: Install the oo CLI from a verified, versioned, signed, or checksum-validated source, and avoid running curl|bash or irm|iex installer commands from an elevated shell.

Risk: Tianyancha requests depend on OOMOL authentication, connected credentials, and account credit.

Mitigation: Use normal connector actions only after the user has installed the CLI, signed in, connected Tianyancha, and confirmed billing availability when a command reports an auth, connection, scope, credential, or credit error.

## Reference(s):

- [Tianyancha homepage](https://www.tianyancha.com/data)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tianyancha)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused connector calls return JSON data and execution metadata from OOMOL.]

## Skill Version(s):

1.0.3 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
