## Description:

PartnerStack helps agents use the OOMOL oo CLI to read PartnerStack records and create customers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PartnerStack through a connected OOMOL account, including listing customers, deals, leads, and partnerships, retrieving specific customer or partnership records, and creating customers when approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance may lead users or agents to execute remote installer scripts directly in a shell.

Mitigation: Use the official install guide and verify the installer through a trusted method before installation; avoid one-line shell installers when that verification is not possible.

Risk: The skill can create PartnerStack customers through a write action.

Mitigation: Confirm the exact customer-creation payload and expected effect with the user before running the write action.

Risk: PartnerStack access depends on OOMOL acting as an intermediary for account credentials and connector execution.

Mitigation: Install and use the skill only when the user accepts OOMOL as the intermediary for PartnerStack operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-partnerstack)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [PartnerStack homepage](https://partnerstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to return JSON from the oo CLI when run with --json.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
