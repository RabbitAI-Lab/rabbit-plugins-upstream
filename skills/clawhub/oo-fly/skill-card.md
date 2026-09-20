## Description:

This skill operates Fly.io apps and Machines through an OOMOL-connected account, including reads plus confirmed write and destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Fly.io apps and Machines from an agent workflow after connecting Fly.io through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fly.io write or destructive actions can change or stop running Machines.

Mitigation: Confirm the target, payload, and expected effect with the user before running actions tagged [write] or [destructive].

Risk: Fly.io operations are routed through OOMOL and require a connected account with Fly.io access.

Mitigation: Install only when comfortable routing Fly.io operations through OOMOL, and grant the connected account only the access needed for the task.

Risk: First-time setup may use remote installer commands for the oo CLI.

Mitigation: Prefer OOMOL's verified installation instructions and review installer commands before execution.

## Reference(s):

- [ClawHub Fly.io skill page](https://clawhub.ai/oomol/skills/oo-fly)
- [Fly.io homepage](https://fly.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from the OOMOL Fly.io connector.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
