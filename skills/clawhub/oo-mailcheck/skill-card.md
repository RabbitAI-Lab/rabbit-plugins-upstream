## Description:

Mailcheck helps agents check account status, validate domains, and verify individual email addresses through a connected Mailcheck/UserCheck account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to check Mailcheck/UserCheck account usage, validate domain risk and MX signals, and verify individual email deliverability and risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts with local code-execution authority.

Mitigation: Use official, versioned, signed, or checksum-verified oo CLI installation instructions before running connector commands.

Risk: Domain and email values are processed through OOMOL/Mailcheck and may consume account credits.

Mitigation: Confirm the data to be checked and expected credit usage before submitting large or sensitive Mailcheck queries.

## Reference(s):

- [ClawHub Mailcheck skill page](https://clawhub.ai/oomol/skills/oo-mailcheck)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Mailcheck homepage](https://www.usercheck.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include Mailcheck/UserCheck data and an execution id when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
