## Description:

Ringg AI uses the OOMOL ringg_ai connector to read, create, and update Ringg AI workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Ringg AI connector schemas and run OOMOL connector actions for assistants, calls, voices, workspace details, caller numbers, and outbound call initiation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes commands that execute remotely downloaded installer scripts.

Mitigation: Review the installer source or install the oo CLI directly from a trusted OOMOL source before allowing an agent to run setup commands.

Risk: The initiate_call action can start an outbound Ringg AI call and change workspace state.

Mitigation: Confirm the exact payload, caller number, assistant, recipient, and intended effect with the user before executing the write action.

## Reference(s):

- [ClawHub Ringg AI Skill](https://clawhub.ai/oomol/skills/oo-ringg-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Ringg AI homepage](https://www.ringg.ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
