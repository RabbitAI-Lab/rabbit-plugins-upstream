## Description:

Diffbot lets agents extract normalized article data from public URLs through an OOMOL-connected Diffbot account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent inspect Diffbot connector schemas and run article extraction for public URLs through their connected OOMOL and Diffbot accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Install the oo CLI through a verified, versioned method that can be inspected, and do not allow an agent to run the remote installer automatically.

Risk: The skill depends on OOMOL as the Diffbot access layer.

Mitigation: Use the skill only after deliberately signing in to OOMOL and connecting the intended Diffbot account and scopes.

## Reference(s):

- [ClawHub Diffbot Skill](https://clawhub.ai/oomol/skills/oo-diffbot)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Diffbot Homepage](https://www.diffbot.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs through the oo CLI connector and returns connector data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
