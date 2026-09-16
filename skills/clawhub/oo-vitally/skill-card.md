## Description:

Vitally (vitally.io). Use this skill for ANY Vitally request - reading, creating, updating, and deleting data. Whenever a task involves Vitally, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and customer success operators use this skill to manage Vitally accounts through the OOMOL-connected oo CLI, including listing, reading, creating, updating, and deleting account records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that first-time setup fallback instructions include remote shell installer commands.

Mitigation: Review the skill before installation, install the oo CLI through a trusted and reviewable method, and do not let an agent run curl-to-bash or irm-to-iex installer commands automatically.

Risk: The skill can create, update, and delete Vitally account records.

Mitigation: Require explicit user approval for every create, update, or delete action and confirm the exact payload and target before execution.

## Reference(s):

- [ClawHub Vitally skill page](https://clawhub.ai/oomol/skills/oo-vitally)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vitally homepage](https://www.vitally.io/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live action schemas before requests and to require confirmation for write or destructive Vitally actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
