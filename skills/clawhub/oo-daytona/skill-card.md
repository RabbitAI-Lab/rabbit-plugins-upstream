## Description:

Daytona connector skill for reading, creating, updating, and deleting Daytona sandboxes through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Daytona sandboxes from an agent workflow through the OOMOL oo CLI. It supports listing, inspecting, creating, starting, stopping, and deleting sandboxes after checking the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes mutable remote installer commands for the oo CLI.

Mitigation: Review or replace the installer commands with a verified installation method before installing the CLI.

Risk: The skill can create, start, stop, and delete Daytona sandboxes through the connected OOMOL account.

Mitigation: Confirm exact payloads for state-changing actions and require explicit approval before destructive deletions.

## Reference(s):

- [Daytona homepage](https://www.daytona.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Daytona skill page](https://clawhub.ai/oomol/skills/oo-daytona)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live Daytona action schemas before constructing payloads; state-changing and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
