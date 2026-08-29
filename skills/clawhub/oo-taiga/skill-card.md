## Description:

Taiga (taiga.io). Use this skill for Taiga requests, including reading, creating, and updating project management data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Taiga projects, issues, tasks, and user stories from an OOMOL-connected account. It supports listing and retrieving Taiga records as well as creating and updating them after reviewing write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Taiga records through a connected OOMOL account.

Mitigation: Review the exact write payload and expected effect with the user before running actions tagged as write.

Risk: The skill depends on OOMOL account access and Taiga connection state.

Mitigation: Only perform one-time CLI installation, authentication, or connection setup when a command fails for that reason and the user trusts OOMOL for the connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-taiga)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Taiga Homepage](https://taiga.io)
- [OOMOL Taiga Connection](https://console.oomol.com/app-connections?provider=taiga)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require payload and effect review before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
