## Description:

Demodesk (demodesk.com). Use this skill for ANY Demodesk request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users with a connected Demodesk account use this skill to read Demodesk users, recordings, transcripts, scorecards, and AI-generated summaries through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can run a remote oo CLI installer script directly on the user's machine.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI only from a trusted, preferably pinned and verified release.

Risk: The skill can read Demodesk business data available to the connected account.

Mitigation: Use an account with appropriate access and limit agent use to the disclosed read-only Demodesk actions unless a future version clearly discloses and gates write actions.

## Reference(s):

- [Demodesk homepage](https://demodesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Demodesk skill page](https://clawhub.ai/oomol/skills/oo-demodesk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first action execution and returns Demodesk connector data when commands are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
