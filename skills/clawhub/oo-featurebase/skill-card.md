## Description:

Featurebase (featurebase.app) skill for reading, creating, updating, and deleting Featurebase data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Featurebase schemas and perform user-directed workspace actions such as listing boards, reading posts, creating feedback, updating posts, and managing contacts through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create feedback, update posts, upsert contacts, and delete Featurebase posts or contacts.

Mitigation: Review the exact action payload and expected effect before approving write actions, and require explicit confirmation for destructive actions.

Risk: First-time setup includes shell-based CLI installation commands.

Mitigation: Verify the OOMOL CLI installer or use the documented install guide before running setup commands.

Risk: Actions operate through an OOMOL-connected Featurebase workspace using server-side credentials.

Mitigation: Install only when the agent is intended to operate that workspace, and ensure the connected account has appropriate permissions.

## Reference(s):

- [Featurebase homepage](https://www.featurebase.app/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill page](https://clawhub.ai/oomol/skills/oo-featurebase)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
