## Description:

Enables agents to read and manage Beeminder users, goals, and datapoints through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Beeminder account data and create, update, or delete goal datapoints through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may ask users to execute remote installer scripts for the OOMOL CLI.

Mitigation: Review the setup step carefully; prefer a pinned, signed, or package-manager install source and only run OOMOL installer endpoints when trusted.

Risk: Write and destructive Beeminder actions can change or remove datapoints.

Mitigation: Confirm the exact payload, effect, and target with the user before running write actions, and require explicit approval before destructive deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-beeminder)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Beeminder homepage](https://www.beeminder.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
