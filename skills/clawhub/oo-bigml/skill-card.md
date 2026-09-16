## Description:

BigML helps agents operate BigML through the OOMOL-connected oo CLI for reading, creating, updating, and deleting BigML resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect BigML action schemas, list or retrieve BigML models and predictions, create predictions, poll prediction results, and delete prediction resources through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may encourage direct execution of remote installer scripts.

Mitigation: Use an existing reviewed oo CLI installation when possible, or download and verify a version-pinned installer before running it.

Risk: The skill can create predictions and delete stored BigML prediction resources.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before any write or destructive action.

## Reference(s):

- [BigML homepage](https://bigml.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bigml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector schema requests, JSON payload examples, and confirmation prompts for write or destructive BigML actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
