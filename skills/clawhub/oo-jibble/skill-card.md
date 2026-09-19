## Description:

Jibble (jibble.io). Use this skill for ANY Jibble request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Jibble through an OOMOL-connected account, including reading organizations, members, and work locations and managing work locations when approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes an unverified internet installer run directly in a shell.

Mitigation: Review the installer before use and prefer installing the oo CLI from a pinned, verified source.

Risk: The skill can create, update, archive, and permanently delete Jibble work locations.

Mitigation: Confirm the exact organization, target location, payload, and expected effect before approving write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jibble)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Jibble homepage](https://www.jibble.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI and live connector schemas before building request payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
