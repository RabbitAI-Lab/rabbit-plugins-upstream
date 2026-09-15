## Description:

Use this skill for Codacy requests that search and read account, organization, repository analysis, language, tool, and pattern data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect live Codacy action schemas and retrieve Codacy user, organization, repository analysis, language, tool, and pattern data through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path documents remote installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer a pinned, checksum- or signature-verified installer before deployment.

Risk: The connected OOMOL account can expose Codacy data available to its credential.

Mitigation: Use the least-privileged Codacy credential available and limit use to trusted agents and workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-codacy)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Codacy homepage](https://www.codacy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Codacy connector runs return JSON responses with data and meta.executionId when actions are executed.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
