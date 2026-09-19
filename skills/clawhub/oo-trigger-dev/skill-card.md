## Description:

Trigger.dev helps agents operate Trigger.dev through an OOMOL-connected account using the oo CLI to inspect connector schemas and run read or state-changing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, cancel, replay, and trigger Trigger.dev runs through a connected OOMOL account while checking live action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified method and review installer commands before allowing an agent to run them.

Risk: The replay_run action can repeat a previous Trigger.dev run and may cause state changes or external side effects.

Mitigation: Treat replay_run as a write or high-impact action and require explicit confirmation of the run ID and expected side effects before execution.

Risk: Write actions such as cancel_run and trigger_task change Trigger.dev state.

Mitigation: Confirm the exact payload and intended effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trigger-dev)
- [Trigger.dev homepage](https://trigger.dev)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
