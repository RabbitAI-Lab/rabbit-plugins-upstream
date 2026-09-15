## Description:

Provides Raygun account operations through the OOMOL oo CLI connector for reading, creating, updating, and deleting Raygun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Raygun applications, deployments, and crash reporting error groups, and to manage Raygun deployments through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes mutable remote installer commands executed directly in a shell.

Mitigation: Prefer a verified package, pinned release, or separately downloaded installer that can be inspected before execution.

Risk: Raygun write and destructive actions can change or delete deployment data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: Raygun operations route through OOMOL as an intermediary with access to the connected Raygun account.

Mitigation: Install only when that intermediary access model is acceptable and the Raygun connection has appropriate account scope.

## Reference(s):

- [Raygun homepage](https://raygun.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Raygun skill on ClawHub](https://clawhub.ai/oomol/skills/oo-raygun)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Raygun connector actions through the oo CLI when the agent follows the skill instructions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
