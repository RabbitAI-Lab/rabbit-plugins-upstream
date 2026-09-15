## Description:

This skill helps agents inspect Bitrise action schemas, list apps and builds, retrieve builds, and trigger Bitrise builds through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to inspect Bitrise connector schemas, read app and build information, and trigger builds or pipelines from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe scripts directly into a shell or PowerShell.

Mitigation: Install the oo CLI through a verified, user-controlled process and do not let an agent run those installer commands automatically.

Risk: The trigger_build action can change Bitrise state by starting a build or pipeline.

Mitigation: Confirm the exact app, action payload, and expected effect with the user before running write actions.

Risk: Authentication, connection, and billing recovery steps require account-level user action.

Mitigation: Run setup or account recovery guidance only after matching command failures, and keep user-controlled account actions explicit.

## Reference(s):

- [ClawHub Bitrise skill page](https://clawhub.ai/oomol/skills/oo-bitrise)
- [Bitrise homepage](https://bitrise.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Bitrise actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
