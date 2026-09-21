## Description:

Knock lets an agent manage Knock users and trigger workflows through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Knock connector schemas, list or retrieve Knock users, identify or update users, delete users with explicit approval, and trigger workflows from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can execute an unpinned remote installer script for the oo CLI.

Mitigation: Review the official installer or install the oo CLI manually from official documentation before using the skill.

Risk: The skill can manage Knock users and trigger workflows through OOMOL-connected tooling.

Mitigation: Install only when that access is acceptable, and confirm exact payloads before write or delete actions.

Risk: The delete_user action permanently deletes a Knock user and associated data.

Mitigation: Require explicit approval of the target user before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-knock)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Knock Homepage](https://knock.app/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
