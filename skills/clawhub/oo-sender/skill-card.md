## Description:

Sender (sender.net). Use this skill for Sender requests that read, create, update, and delete data through the OOMOL-connected Sender connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Sender marketing resources from an agent through the OOMOL `oo` CLI. It supports reading campaigns, groups, subscribers, fields, and workflows, and it can create or update subscriber-related resources when the user confirms the intended change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute changing network content on a user machine.

Mitigation: Review the oo CLI installation path before installing, prefer verified official releases or a trusted package manager, and do not let an agent run the curl-to-bash or PowerShell iex commands automatically.

Risk: Write actions can change Sender state, and the destructive group-removal action can remove subscribers from groups.

Mitigation: Require confirmation of the exact payload and expected effect before write actions, and require explicit approval for destructive operations.

## Reference(s):

- [Sender homepage](https://www.sender.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sender)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before constructing payloads and returns connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: server evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
