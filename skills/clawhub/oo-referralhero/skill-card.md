## Description:

ReferralHero lets agents read, create, update, and delete ReferralHero data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage ReferralHero campaigns, subscribers, rewards, leaderboards, and conversion events from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change ReferralHero campaign or subscriber state.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: The delete subscriber action removes account data.

Mitigation: Confirm the target subscriber and obtain explicit user approval before running destructive actions.

Risk: Pipe-to-shell installer commands can execute remote code during setup.

Mitigation: Use a safer official installation path or independently verify the installer source before running the command.

## Reference(s):

- [ReferralHero homepage](https://referralhero.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ReferralHero skill page](https://clawhub.ai/oomol/skills/oo-referralhero)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live connector schema before running actions; oo CLI responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
