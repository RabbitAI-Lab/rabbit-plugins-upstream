## Description:

This skill helps agents operate Replicate through an OOMOL-connected account by inspecting live action schemas and running read or write actions for predictions, models, versions, collections, and account details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage Replicate resources through the OOMOL-connected oo CLI, including creating or canceling predictions and reading models, versions, collections, predictions, and account details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute downloaded shell or PowerShell code locally.

Mitigation: Review the setup path before installation and prefer a verified, versioned oo CLI release or package manager.

Risk: Create and cancel actions can change Replicate account state or spend account resources.

Mitigation: Confirm the exact action payload and expected effect with the user before running create_prediction or cancel_prediction.

## Reference(s):

- [Replicate homepage](https://replicate.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Replicate skill page](https://clawhub.ai/oomol/skills/oo-replicate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before constructing payloads and to confirm write or destructive actions before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
