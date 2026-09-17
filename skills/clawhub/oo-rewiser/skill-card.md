## Description:

Rewiser enables agents to read, create, and update Rewiser data through the OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Rewiser folders and transactions through an OOMOL-connected account. It supports listing folders, retrieving recent transactions with filters, and creating multiple transactions after user confirmation for write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could be unsafe if run blindly or without integrity checks.

Mitigation: Use official, versioned installation instructions, inspect installers before execution, and avoid running curl-to-shell or PowerShell pipe commands automatically.

Risk: Write actions can create incorrect Rewiser transactions if the payload is wrong.

Mitigation: Fetch the live action schema, show the exact payload and intended effect to the user, and run write actions only after explicit confirmation.

## Reference(s):

- [Rewiser homepage](https://rewiser.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rewiser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
