## Description:

Featurebase helps agents read, create, update, and delete Featurebase boards, posts, and contacts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Featurebase feedback workflows for an authenticated organization, including listing boards, posts, and contacts and performing confirmed create, update, upsert, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run oo CLI commands against a connected Featurebase account, including write and delete actions.

Mitigation: Install only if you trust OOMOL, inspect generated payloads, and require explicit approval before write or destructive actions.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer verified official release or package-manager installation steps and review installer commands before running them.

## Reference(s):

- [Featurebase homepage](https://www.featurebase.app/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
