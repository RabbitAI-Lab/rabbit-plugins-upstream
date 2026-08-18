## Description:

Operate LoyJoy through an OOMOL-connected account by inspecting live connector schemas and running LoyJoy connector actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, retrieve, search, and run LoyJoy tenant processes and home views through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change LoyJoy tenant state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Read and search actions may expose tenant knowledge base, process, or view data available to the connected account.

Mitigation: Install and use the skill only for authorized LoyJoy account access, and limit queries to the user's intended task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-loyjoy)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [LoyJoy homepage](https://www.loyjoy.com/en/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.0 (source: server evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
