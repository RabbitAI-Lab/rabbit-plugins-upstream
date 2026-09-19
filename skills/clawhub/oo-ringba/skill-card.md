## Description:

Ringba (ringba.com). Use this skill for searching and reading Ringba account data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Ringba account details, campaigns, phone numbers, and publishers through the oo CLI after Ringba is connected in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions run mutable remote installer scripts, which can execute local code if an installer endpoint is compromised.

Mitigation: Review the installer path before installing. Prefer a signed or verified package, or download and inspect the installer before running it.

## Reference(s):

- [ClawHub Ringba skill](https://clawhub.ai/oomol/skills/oo-ringba)
- [Publisher profile: oomol](https://clawhub.ai/user/oomol)
- [Ringba homepage](https://www.ringba.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-oriented connector actions; action results are returned as JSON by the oo CLI when commands are run.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
