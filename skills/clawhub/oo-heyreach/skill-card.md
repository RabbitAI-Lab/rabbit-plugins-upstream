## Description:

HeyReach lets an agent read, create, and update HeyReach data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect HeyReach campaigns, leads, lead tags, lead lists, LinkedIn sender accounts, and outreach statistics. They can also create empty HeyReach lead or company lists after confirming the write payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing external code on the user's machine.

Mitigation: Review the OOMOL oo CLI installation path before installing and prefer official, version-pinned installers with checksum or signature verification.

Risk: The skill can create empty HeyReach lead or company lists, which changes HeyReach state.

Mitigation: Confirm the exact HeyReach write action payload and expected effect with the user before running it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-heyreach)
- [HeyReach Homepage](https://www.heyreach.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running HeyReach actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
