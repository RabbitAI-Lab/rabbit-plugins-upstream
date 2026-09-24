## Description:

DAMI helps agents operate DAMI TikTok Shop workflows through OOMOL's dami_mcp connector for reading, creating, updating, and deleting DAMI data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect DAMI action schemas and run authorized DAMI TikTok Shop discovery, creator outreach, account, and operations workflows through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote oo CLI installer commands could execute unreviewed shell or PowerShell code during first-time setup.

Mitigation: Install the oo CLI through a trusted, verified method and review installer behavior before execution.

Risk: DAMI write or destructive actions can send creator messages, create outreach tasks, change workflow configuration, or consume credits.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user, and require explicit approval before running state-changing actions.

## Reference(s):

- [DAMI homepage](https://www.tikclubs.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub DAMI skill page](https://clawhub.ai/oomol/skills/oo-dami-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing DAMI actions are labeled as write or destructive and require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
