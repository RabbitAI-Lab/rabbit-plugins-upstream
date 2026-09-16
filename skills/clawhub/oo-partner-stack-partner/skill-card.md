## Description:

PartnerStack Partner (partnerstack.com). Use this skill for ANY PartnerStack Partner request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to query PartnerStack Partner data through an OOMOL-connected account, including marketplace programs, partnerships, payouts, and rewards. It is intended for schema-first read workflows that call the oo CLI rather than constructing PartnerStack API calls directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PartnerStack payout, reward, partnership, and account data may pass through OOMOL during use.

Mitigation: Use the skill only with an approved OOMOL-connected account and avoid requesting or exposing sensitive PartnerStack data unless it is necessary for the task.

Risk: The first-time setup guidance includes remote installer commands for the oo CLI.

Mitigation: Verify the oo CLI installation source and use a trusted installation path before running setup commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-partner-stack-partner)
- [PartnerStack Homepage](https://partnerstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON output from oo CLI actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return PartnerStack data through OOMOL with an execution id under meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
