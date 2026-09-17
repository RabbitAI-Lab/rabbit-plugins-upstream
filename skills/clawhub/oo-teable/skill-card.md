## Description:

Teable (teable.cn) skill for reading, creating, updating, and deleting Teable data through the OOMOL-connected connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Teable through an OOMOL-connected account, including reading users, spaces, bases, tables, records, and record details. It also supports creating, updating, and permanently deleting records when the user confirms the intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts directly without verification.

Mitigation: Review the skill before installing the oo CLI and prefer a signed package, pinned release, or separately downloaded installer with verified checksum or signature.

Risk: The skill can create, update, and permanently delete Teable records.

Mitigation: Confirm the exact payload, affected record, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [Teable homepage](https://teable.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-teable)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before constructing payloads and requires confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
