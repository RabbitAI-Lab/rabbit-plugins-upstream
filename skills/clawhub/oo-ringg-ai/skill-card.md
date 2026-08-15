## Description:

Ringg AI helps an agent operate a connected Ringg AI workspace through OOMOL's `oo` CLI for assistant, voice, workspace number, call history, call detail, and outbound call workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to inspect Ringg AI workspace resources, retrieve call records, and initiate outbound calls when the user has connected Ringg AI through OOMOL. It is intended for account-backed Ringg AI workflows where the agent should use the connector rather than handling API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate outbound phone calls, and the security evidence notes that this risk is under-disclosed in the current documentation.

Mitigation: Require explicit user confirmation before any `initiate_call` use, including the target number, caller number, assistant, and intended call purpose.

Risk: Read-only list and get actions may expose workspace, assistant, voice, phone number, call history, or call analysis data.

Mitigation: Limit requests to the user-authorized Ringg AI workspace and return only the data needed for the user's task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ringg-ai)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Ringg AI homepage](https://www.ringg.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
