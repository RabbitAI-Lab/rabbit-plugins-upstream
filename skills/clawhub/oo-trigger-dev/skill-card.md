## Description:

Trigger.dev helps agents operate Trigger.dev through an OOMOL-connected account for reading runs, retrieving results, triggering tasks, replaying runs, and canceling in-progress runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Trigger.dev action schemas and run Trigger.dev connector actions through the oo CLI. It supports read workflows for run inspection and guarded state-changing workflows for triggering tasks, replaying runs, and canceling in-progress runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger tasks, replay runs, and cancel in-progress Trigger.dev runs, which may change account state.

Mitigation: Confirm the exact payload, target run or task, and expected effect with the user before running write or destructive actions.

Risk: The skill relies on OOMOL as the connector layer for the user's Trigger.dev account.

Mitigation: Install only when the user is comfortable with that connector layer and has connected the intended Trigger.dev account.

Risk: First-time setup may require running an oo CLI installer from the network.

Mitigation: Review the install source or use an official verified installation path before running one-time installer commands.

## Reference(s):

- [Trigger.dev homepage](https://trigger.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trigger-dev)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector commands that return JSON responses from Trigger.dev actions.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
