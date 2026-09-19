## Description:

Provides agent guidance for using the OOMOL oo CLI to inspect Ahrefs connector schemas and retrieve keyword, usage, and Site Explorer data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Ahrefs data through an OOMOL-connected account, including keyword overview rows, usage limits, and Site Explorer metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include an unverified remote installer executed directly in a shell.

Mitigation: Use official installation documentation, pinned releases, and checksum or signature verification before running an installer.

Risk: The skill depends on OOMOL and the oo CLI to handle Ahrefs access.

Mitigation: Install only when the user trusts OOMOL and is comfortable with the oo CLI mediating Ahrefs credentials and actions.

## Reference(s):

- [Ahrefs homepage](https://ahrefs.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Ahrefs skill page](https://clawhub.ai/oomol/skills/oo-ahrefs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to fetch live connector schemas before constructing Ahrefs action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
