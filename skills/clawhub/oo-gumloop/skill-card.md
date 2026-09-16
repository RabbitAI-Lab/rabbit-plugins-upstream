## Description:

Gumloop lets an agent inspect schemas and operate Gumloop workbooks, saved flows, run history, and flow runs through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list Gumloop assets, inspect saved flow schemas, start flow runs, and monitor or stop active runs from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the OOMOL CLI.

Mitigation: Install the CLI through a verified official package or inspect a versioned installer before running setup commands.

Risk: Starting or killing Gumloop flow runs can affect live Gumloop work.

Mitigation: Require explicit user confirmation for start_flow_run and kill_flow_run, including the target flow or run and payload.

## Reference(s):

- [Gumloop homepage](https://www.gumloop.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gumloop)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Gumloop action schemas before constructing command payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
