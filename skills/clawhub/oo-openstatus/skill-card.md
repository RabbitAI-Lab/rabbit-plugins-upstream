## Description:

OpenStatus helps an agent read, create, update, delete, list, and inspect OpenStatus monitors through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage OpenStatus monitors, inspect monitor health and logs, trigger checks, and retrieve summary metrics from an authenticated OOMOL-connected workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the CLI only from a trusted, versioned, verifiable source or inspect the installer before running it.

Risk: Write and delete actions can change or remove OpenStatus monitor data.

Mitigation: Confirm the exact target, payload, and expected effect before approving write or destructive actions.

## Reference(s):

- [OpenStatus homepage](https://www.openstatus.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub OpenStatus skill page](https://clawhub.ai/oomol/skills/oo-openstatus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live OpenStatus action schemas before constructing command payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
