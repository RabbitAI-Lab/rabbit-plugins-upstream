## Description:

Operate KnowBe4 through an OOMOL-connected account to inspect schemas and read account, user, and group data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve KnowBe4 account, subscription, group, and user data through an OOMOL-connected account while keeping credentials server-side.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not let an agent run those installer commands automatically; use a verified, pinned, or checksum-checked oo CLI installation path before using the skill.

Risk: The skill depends on connecting KnowBe4 through OOMOL.

Mitigation: Use it only when the user is comfortable with that connection path and has already connected the account or explicitly approves the setup.

## Reference(s):

- [ClawHub KnowBe4 Skill](https://clawhub.ai/oomol/skills/oo-knowbe4)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [KnowBe4 Homepage](https://www.knowbe4.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live connector schema before execution and use server-side credentials through OOMOL.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
