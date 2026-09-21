## Description:

Wachete lets agents operate Wachete through the OOMOL-connected oo CLI to read, create, update, and delete monitor data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Wachete monitors through an authenticated OOMOL connector, including listing folders and notifications, reviewing monitor history, and creating, replacing, or deleting monitors with explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remotely downloaded installer commands for the oo CLI.

Mitigation: Review or install the CLI through trusted manual or package-manager steps before allowing remote installer execution.

Risk: The skill can create, replace, or delete Wachete monitors.

Mitigation: Require explicit user approval for the exact target, payload, and effect before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wachete)
- [Wachete homepage](https://www.wachete.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
