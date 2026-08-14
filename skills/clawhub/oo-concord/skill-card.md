## Description:

Concord (concord.app). Use this skill for ANY Concord request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search and read Concord profile, organization, agreement, and folder information available to their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agreement and organization listings may contain business-sensitive information.

Mitigation: Install and run the skill only for accounts where the agent is allowed to read Concord data, and review returned information before sharing it.

Risk: Future versions could add write or destructive Concord actions.

Mitigation: Review future release notes and security findings before upgrading, and require explicit user confirmation before any action that changes or deletes data.

## Reference(s):

- [Concord homepage](https://www.concord.app/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-concord)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for running read-only Concord connector actions through the OOMOL oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
