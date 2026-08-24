## Description:

福昕 Office 连接助手 provides a preflight readiness check for Foxit/Fuxin Office integrations, verifying local installation, bridge connectivity, product registration, backend reachability, and active document status before document operations proceed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foxitnet](https://clawhub.ai/user/foxitnet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill as an infrastructure preflight before Foxit/Fuxin Office document workflows. It checks whether the local Office installation, Agent Bridge, registered products, backend endpoints, and active documents are ready, then returns concise readiness guidance for the next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects local Office installation state, running processes, local Agent Bridge status, and active document paths/status.

Mitigation: Use it only for explicit Foxit/Fuxin Office readiness checks and review diagnostic output before continuing with document operations.

Risk: Generic preflight wording could activate the skill when the user did not intend a Foxit/Fuxin Office check.

Mitigation: Prefer explicit Foxit/Fuxin Office commands such as checking Office readiness or Agent Bridge status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foxitnet/skills/fuxin-office-bridge)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with PowerShell examples and readiness status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces readiness states, diagnostic messages, and active document details when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
