## Description:

ReferralHero connector skill for reading, creating, updating, and deleting ReferralHero campaign and subscriber data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ReferralHero referral campaigns and subscriber workflows from an agent. It supports campaign listing and creation, subscriber management, leaderboards, rewards, conversion tracking, and referral confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete ReferralHero campaign and subscriber data through the connected OOMOL account.

Mitigation: Review payloads carefully and require clear user approval before write or destructive actions.

Risk: Incorrect action input can affect the wrong campaign or subscriber.

Mitigation: Inspect the live connector schema before execution and confirm the target identifier and expected effect.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-referralhero)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ReferralHero](https://referralhero.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo connector; live schema inspection is expected before payload construction.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
