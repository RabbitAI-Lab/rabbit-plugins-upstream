## Description:

Get Biji (biji.com). Use this skill for ANY Get Biji request: reading, creating, updating, and deleting data through the OOMOL getnote connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Get Biji notes, tags, knowledge bases, bloggers, and live-session content through an authenticated OOMOL-connected account. It supports read, search, create, update, sharing, and deletion workflows while requiring confirmation for writes and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's fallback setup includes remote installer commands for the oo CLI, and the security summary flags those installer commands as unverified.

Mitigation: Review the skill before installing, and prefer installing the oo CLI through a verified, pinned, or inspectable method before allowing an agent to run connector actions.

Risk: Write and destructive actions can change or remove Get Biji data.

Mitigation: Require confirmation of the exact payload, target, and expected effect before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-getnote)
- [Get Biji Homepage](https://www.biji.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Get Biji Service Icon](https://static.oomol.com/logo/third-party/getnote.png)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
