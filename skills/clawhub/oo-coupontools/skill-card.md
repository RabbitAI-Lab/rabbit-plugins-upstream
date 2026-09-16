## Description:

Coupontools helps agents list coupon campaigns, inspect individual campaigns, and create single-use coupon URLs through an OOMOL-connected Coupontools account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Coupontools campaigns from an agent workflow, including reading campaign data and creating single-use coupon URLs after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Install the oo CLI only from a verified package or documented release with integrity checks before using the skill.

Risk: The create_single_use_url action changes Coupontools state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Coupontools Skill](https://clawhub.ai/oomol/skills/oo-coupontools)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Coupontools Homepage](https://www.coupontools.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector requests; write actions require user confirmation of payload and effect.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
