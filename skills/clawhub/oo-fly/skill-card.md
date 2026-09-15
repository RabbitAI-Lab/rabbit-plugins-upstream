## Description:

Fly.io (fly.io). Use this skill for ANY Fly.io request - reading, creating, and updating data. Whenever a task involves Fly.io, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Fly.io connector schemas, run Fly.io actions through the OOMOL-connected oo CLI, and manage Fly Apps and Machines with confirmation before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may lead users to execute unverified remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution path and inspect or verify installer artifacts before execution.

Risk: Fly.io actions are routed through OOMOL-connected services rather than direct local Fly.io credentials.

Mitigation: Use the skill only when routing Fly.io connector actions through OOMOL is acceptable for the account and workload.

Risk: Create, start, stop, and restart actions can change Fly.io resource state.

Mitigation: Require explicit user confirmation for the exact target, payload, and expected effect before running state-changing actions.

## Reference(s):

- [Fly.io homepage](https://fly.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fly)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema inspection commands, JSON action payload guidance, and execution identifiers returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
