## Description:

Formspree lets an agent search and read Formspree submissions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect the Formspree connector schema and list submissions for a connected Formspree form through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell and PowerShell installer commands.

Mitigation: Install the oo CLI through a verified, trusted method and do not allow an agent to automatically execute curl-to-bash or PowerShell iex installers.

Risk: Formspree data is accessed through an OOMOL-connected account with credentials injected server-side.

Mitigation: Review what Formspree data and scopes the OOMOL connection exposes before using the skill.

## Reference(s):

- [ClawHub Formspree Skill Page](https://clawhub.ai/oomol/skills/oo-formspree)
- [Formspree Homepage](https://formspree.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; available action output is JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
