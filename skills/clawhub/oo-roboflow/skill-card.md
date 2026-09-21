## Description:

Provides OOMOL-connected access to Roboflow for reading, creating, and updating Roboflow data through the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to operate Roboflow through an OOMOL-connected account, including project discovery, inference, workflow validation, and workflow execution. It helps agents inspect connector schemas before constructing Roboflow payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer official installation documentation or verify the installer source and contents before running the commands.

Risk: Workflow execution actions can change Roboflow state.

Mitigation: Review the exact workflow payload and expected effect with the user before approving write actions, and require explicit approval before any destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-roboflow)
- [Roboflow Homepage](https://roboflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands, JSON payload guidance, and summaries of JSON connector responses.]

## Skill Version(s):

1.0.4 (source: server evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
