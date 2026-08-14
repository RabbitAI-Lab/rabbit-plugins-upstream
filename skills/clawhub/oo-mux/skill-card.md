## Description:

Mux (mux.com). Use this skill for ANY Mux request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Mux video assets, direct uploads, playback IDs, and asset metadata through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Mux assets, direct uploads, playback IDs, or metadata in the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can permanently delete Mux video assets and their data.

Mitigation: Require explicit approval for the target asset before running destructive actions.

Risk: Authentication, connection, or billing failures can block connector actions.

Mitigation: Use first-time setup or account remediation steps only after a command fails with the matching error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mux)
- [Mux homepage](https://www.mux.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
