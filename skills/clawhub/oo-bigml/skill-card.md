## Description:

BigML lets an agent inspect BigML connector schemas, list and retrieve models and predictions, create predictions, and delete stored prediction resources through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate BigML resources from an OOMOL-connected account without handling raw BigML credentials. It supports schema inspection, model and prediction lookup, prediction creation, polling, and explicitly confirmed prediction deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow recommends executing remote installer scripts directly in a shell.

Mitigation: Use an official verified installer or review the downloaded installer before execution; do not allow an agent to run curl|bash or irm|iex commands blindly.

Risk: The skill can create BigML predictions and delete stored prediction resources.

Mitigation: Require explicit user confirmation for state-changing or destructive actions, including the exact payload, resource identifier, and expected effect.

Risk: The skill depends on the OOMOL oo CLI and BigML connector for authenticated execution.

Mitigation: Install only when the publisher, CLI, and connector are trusted, and handle authentication or connection setup only after a command fails for that specific reason.

## Reference(s):

- [BigML homepage](https://bigml.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub BigML skill page](https://clawhub.ai/oomol/skills/oo-bigml)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and may return connector JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
