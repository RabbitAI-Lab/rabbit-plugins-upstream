## Description:

The ntfy skill lets agents inspect ntfy connector schemas, retrieve account details, and publish notifications through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate ntfy through an OOMOL-connected account, including account inspection and notification publishing. It is useful when an agent needs connector-backed ntfy access without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include online installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI manually through a trusted and verifiable path before using the skill.

Risk: The publish_message action changes ntfy state by sending a notification to a topic.

Mitigation: Require explicit user confirmation of the exact topic, message, and expected effect before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ntfy)
- [ntfy homepage](https://ntfy.sh)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
