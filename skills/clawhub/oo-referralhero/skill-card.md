## Description:

ReferralHero helps agents manage ReferralHero campaigns, subscribers, referrals, rewards, and conversion workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect and manage ReferralHero referral campaigns, subscribers, referrals, rewards, and conversion events. The skill supports read actions directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that could run arbitrary local code.

Mitigation: Review and independently verify the OOMOL CLI installation source before running installer one-liners.

Risk: Write and destructive ReferralHero actions can change or delete campaign and subscriber data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub ReferralHero skill page](https://clawhub.ai/oomol/skills/oo-referralhero)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ReferralHero homepage](https://referralhero.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the oo CLI and may return JSON responses from ReferralHero connector actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
