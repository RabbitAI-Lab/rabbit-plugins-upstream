## Description:

GoDial (godial.cc). Use this skill for ANY GoDial request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate GoDial through an OOMOL-connected account, including listing accounts, lists, and contacts, fetching contacts, and creating contacts after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review setup steps before installation and prefer an independently verified or package-manager installation of the oo CLI.

Risk: Generated or user-supplied GoDial data can be embedded into shell command payloads.

Mitigation: Use file-based JSON payloads for generated or user-supplied GoDial data.

Risk: The create_contact action changes GoDial account state.

Mitigation: Confirm the exact payload and effect with the user before allowing write actions to run.

## Reference(s):

- [GoDial homepage](https://godial.cc)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-godial)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the OOMOL oo CLI to inspect live connector schemas and run GoDial actions; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
