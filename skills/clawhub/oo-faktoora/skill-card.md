## Description:

Faktoora (faktoora.com) lets an agent read, create, update, and delete Faktoora data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Faktoora projects through an OOMOL-connected account, including listing, retrieving, creating, updating, deleting, attaching, and detaching project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes mutable remote installer commands for the oo CLI without checksum or signature verification.

Mitigation: Install the oo CLI through a verified, version-pinned vendor channel with checksum or signature validation before using the skill.

Risk: The skill can create, update, attach, detach, and permanently delete Faktoora project data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: Using the skill requires connecting a Faktoora account through OOMOL.

Mitigation: Connect only accounts the user is comfortable letting OOMOL use for Faktoora actions.

## Reference(s):

- [Faktoora homepage](https://faktoora.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-faktoora)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing and destructive Faktoora actions require user confirmation; live action schemas are inspected before requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
