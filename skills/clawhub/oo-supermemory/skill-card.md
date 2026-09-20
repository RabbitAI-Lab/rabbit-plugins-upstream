## Description:

Supermemory operates a Supermemory account through OOMOL's oo CLI to read, create, update, and delete documents, memories, recall results, and profile context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Supermemory through an OOMOL-connected account, including adding documents, creating memories, searching recall results, reading profiles, and managing existing memory or document records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance endorses executing remote installer scripts directly in a shell without verification.

Mitigation: Review the oo CLI installation path before installing, prefer official version-pinned instructions with checksum or signature verification, and avoid unverified installer execution.

Risk: Write and destructive Supermemory actions can modify, delete, or overwrite user data.

Mitigation: Confirm the exact payload, effect, and target with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-supermemory)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Supermemory Homepage](https://supermemory.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before action payload construction and explicit confirmation before write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
