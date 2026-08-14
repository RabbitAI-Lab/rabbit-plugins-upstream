## Description:

Raindrop.io lets an agent manage bookmarks, collections, tags, and profile data in a connected Raindrop.io account through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, create, update, search, and delete Raindrop.io bookmarks and collections through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Raindrop.io bookmarks and collections.

Mitigation: Review the exact payload and expected effect before approving write actions, and require explicit approval for destructive actions.

Risk: The one-time CLI installer runs code from the OOMOL installation source.

Mitigation: Run the installer only when the CLI is missing and only if the user trusts the OOMOL installation source.

Risk: The skill operates through an OOMOL-connected Raindrop.io account.

Mitigation: Install and use it only when the user wants an agent to manage that Raindrop.io account through OOMOL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-raindrop)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Raindrop.io homepage](https://raindrop.io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
