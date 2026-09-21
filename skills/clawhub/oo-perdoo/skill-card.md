## Description:

Perdoo (perdoo.com) supports reading, creating, and updating Perdoo data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read Perdoo goals and, after confirming the exact payload and effect, create or update Perdoo data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable actions can update Perdoo state.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write-capable.

Risk: The execute_graphql action can issue broad GraphQL queries or mutations.

Mitigation: Inspect the live action schema and review the GraphQL operation before execution, especially for mutations.

Risk: The first-time setup path includes remote oo CLI installer commands.

Mitigation: Use OOMOL's official installation instructions and verify the installer source before running remote install commands.

## Reference(s):

- [ClawHub Perdoo skill page](https://clawhub.ai/oomol/skills/oo-perdoo)
- [Perdoo homepage](https://www.perdoo.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector commands that return JSON responses from Perdoo actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
