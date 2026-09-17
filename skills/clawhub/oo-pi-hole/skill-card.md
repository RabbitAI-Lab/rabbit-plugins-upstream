## Description:

Pi-hole lets an agent operate a connected Pi-hole instance through OOMOL's oo CLI for reading, creating, updating, and deleting Pi-hole data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Pi-hole status, query DNS activity, manage domains, lists, groups, clients, and configuration, and run operational Pi-hole actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may fetch and execute unpinned code during setup.

Mitigation: Install or update the oo CLI through an official package manager or a reviewed, version-pinned installer before allowing the agent to use it.

Risk: Write and destructive Pi-hole actions can change DNS behavior or remove configuration data.

Mitigation: Confirm exact payloads for write actions and require explicit user approval for destructive deletes or restores.

## Reference(s):

- [Pi-hole homepage](https://pi-hole.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pi-hole)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
