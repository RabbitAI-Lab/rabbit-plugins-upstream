## Description:

Faktoora enables agents to read, create, update, attach, detach, and delete Faktoora project data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Faktoora projects through an OOMOL-connected account, including listing, retrieving, creating, updating, attaching documents, detaching documents, and deleting projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, attach, detach, and permanently delete Faktoora project data through a connected OOMOL account.

Mitigation: Confirm write and delete payloads carefully with the user before execution, especially the target project and intended effect.

Risk: Connector access depends on OOMOL login and a trusted Faktoora connection.

Mitigation: Only complete oo CLI login or Faktoora connection setup when the user trusts OOMOL as the connector provider.

## Reference(s):

- [Faktoora homepage](https://faktoora.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Faktoora skill page](https://clawhub.ai/oomol/skills/oo-faktoora)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
