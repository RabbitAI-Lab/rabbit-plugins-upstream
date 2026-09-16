## Description:

Operate Botsonic through an OOMOL-connected account to generate bot responses and read conversations and FAQs using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Botsonic through an OOMOL-connected account, including generating synchronous bot responses and reading Botsonic conversations and FAQs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute an unverified remote installer directly in the user's shell.

Mitigation: Review the oo CLI installation path before installing; prefer a package manager or pinned release with checksum or signature verification, and require explicit approval before running remote installer commands.

## Reference(s):

- [Botsonic homepage](https://botsonic.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Botsonic skill page](https://clawhub.ai/oomol/skills/oo-botsonic)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
