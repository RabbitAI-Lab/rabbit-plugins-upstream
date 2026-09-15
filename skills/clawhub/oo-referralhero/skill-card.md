## Description:

ReferralHero lets an agent manage ReferralHero campaigns, subscribers, rewards, leaderboards, conversions, and referrals through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ReferralHero account data from an agent, including campaign, subscriber, reward, leaderboard, conversion, and referral workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Do not let an agent run those installers automatically; use official, versioned installation steps with checksum or signature verification.

Risk: Write actions can change ReferralHero campaign or subscriber state.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: The delete_subscriber action removes subscriber data.

Mitigation: Confirm the target subscriber and obtain explicit approval before running destructive actions.

## Reference(s):

- [ReferralHero ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-referralhero)
- [ReferralHero Homepage](https://referralhero.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL ReferralHero Connection](https://console.oomol.com/app-connections?provider=referralhero)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [ReferralHero action responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
