## Description:

Enables agents to read, create, update, and delete Opsgenie data through the OOMOL Opsgenie connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Opsgenie alerts through an OOMOL-connected account, including listing, fetching, creating, acknowledging, and closing alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opsgenie alert state can be changed through write and close actions.

Mitigation: Confirm the exact payload and intended effect with the user before write actions, and require explicit approval before destructive close actions.

Risk: Installer commands can execute remote scripts when the oo CLI is missing.

Mitigation: Use official or verified oo CLI installation steps and avoid blindly running installer scripts.

Risk: Opsgenie data is accessed through an OOMOL-connected account.

Mitigation: Ensure the connected account and scopes are appropriate before running commands that read or modify alert data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-opsgenie)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Opsgenie homepage](https://www.atlassian.com/software/opsgenie)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads and returns connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
