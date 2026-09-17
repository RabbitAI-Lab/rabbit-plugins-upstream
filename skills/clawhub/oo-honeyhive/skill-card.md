## Description:

Operates HoneyHive through an OOMOL-connected account for reading, creating, updating, and deleting datasets and datapoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected HoneyHive account use this skill to inspect HoneyHive connector schemas and run dataset and datapoint operations through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute mutable external code.

Mitigation: Review the setup path before installing and prefer a versioned, verifiable oo CLI source.

Risk: Write and destructive HoneyHive actions can change, remove, or overwrite dataset and datapoint state.

Mitigation: Inspect the live action schema first and require explicit user confirmation for the exact payload and target before running write or destructive actions.

## Reference(s):

- [HoneyHive homepage](https://www.honeyhive.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-honeyhive)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live HoneyHive connector schemas before building action payloads; command responses may include HoneyHive connector JSON.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
