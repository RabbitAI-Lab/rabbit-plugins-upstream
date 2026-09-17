## Description:

Plane (plane.so). Use this skill for reading, creating, updating, and deleting Plane data through the OOMOL-connected oo CLI instead of calling the Plane API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Plane workspaces from an agent, including project, work item, label, state, member, and current-user lookups. With user confirmation, the skill can also create, update, or delete Plane work items through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing mutable remote installer scripts directly in a shell.

Mitigation: Review the installer before use and prefer a pinned, signed, or package-manager-based OOMOL CLI installation path.

Risk: The skill can create, update, and delete Plane work items.

Mitigation: Confirm the exact payload, target, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plane)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Plane homepage](https://plane.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON-shaped connector responses when Plane actions are executed.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
