## Description:

This skill lets agents operate Signaturely through an OOMOL-connected account for supported folder workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Signaturely folder workflows through an OOMOL-connected account, including creating, retrieving, listing, and renaming folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer one-liners that can change over time.

Mitigation: Do not let an agent run those installer commands automatically; install the OOMOL CLI manually from a trusted, versioned source and verify the installer when possible.

Risk: Write actions such as folder creation and renaming change Signaturely account state.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Signaturely homepage](https://signaturely.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-signaturely)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the Signaturely connector when executed with the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
