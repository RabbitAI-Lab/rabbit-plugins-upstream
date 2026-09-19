## Description:

Slab (slab.com). Use this skill for ANY Slab request - reading, creating, updating, and deleting data. Whenever a task involves Slab, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Slab through OOMOL's oo CLI, including reading and searching Slab content and creating, updating, syncing, tagging, or deleting posts and topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer scripts that can run arbitrary code on a user's machine.

Mitigation: Review the installer path before use; prefer a verified or package-manager installation for the oo CLI.

Risk: Write and destructive Slab actions can change or remove workspace content.

Mitigation: Confirm the exact target, payload, and expected effect before allowing write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slab)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Slab Homepage](https://slab.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
