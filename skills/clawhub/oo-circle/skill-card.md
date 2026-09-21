## Description:

Circle (circle.so) lets an agent search and read Circle community, member, post, space group, and space membership data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with an OOMOL-connected Circle account use this skill to inspect Circle community records and run read-oriented connector actions from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute remote oo CLI installer scripts.

Mitigation: Review the installer before execution or use a verified package or release path when available.

Risk: Circle connector scope may exceed the read-only actions currently listed.

Mitigation: Inspect the live action schema before execution and require explicit user confirmation for any write or destructive action, target, and payload.

## Reference(s):

- [Circle homepage](https://circle.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-circle)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and return connector JSON when executed.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
