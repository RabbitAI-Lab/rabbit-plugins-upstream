## Description:

Reddit enables an agent to read, create, update, and delete Reddit content through an OOMOL-connected Reddit account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Reddit profiles, posts, searches, and comments, and to create, edit, or delete authenticated Reddit posts or comments after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit write and destructive actions can create, overwrite, or permanently delete authenticated user content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before creating, editing, or deleting Reddit content.

Risk: CLI installation examples include pipe-to-shell commands.

Mitigation: Review the oo CLI installer source or use an official/manual installation path before running installer commands.

Risk: Reddit actions route through OOMOL's connector and server-side credentials.

Mitigation: Install only when the user is comfortable using OOMOL's Reddit connector and has reviewed the connected account and scopes.

## Reference(s):

- [ClawHub Reddit Skill](https://clawhub.ai/oomol/skills/oo-reddit)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Reddit](https://www.reddit.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns Reddit connector responses with execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
