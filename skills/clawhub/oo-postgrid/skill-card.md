## Description:

PostGrid (postgrid.com). Use this skill for ANY PostGrid request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PostGrid through OOMOL-connected credentials for Print & Mail contact and template workflows, including read, create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can lead an agent to run unverified internet installer scripts with local privileges.

Mitigation: Install the oo CLI through an official, pinned, and verified path, and do not allow the agent to run curl-to-bash or PowerShell iex installers blindly.

Risk: Write and destructive PostGrid actions can create, update, or delete contacts and templates.

Mitigation: Confirm the exact payload, target, and expected effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [PostGrid homepage](https://www.postgrid.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-postgrid)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
