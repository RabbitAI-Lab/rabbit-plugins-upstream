## Description:

Use before claiming work is successful or complete, or relaying a tool or subagent success report, to require fresh verification evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[escoffier-labs](https://clawhub.ai/user/escoffier-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill before reporting work as successful or complete. It requires running a fresh, whole proving command, inspecting its output and exit status, and reporting only what the evidence supports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification capture or conditional ledger export may retain or expose command output.

Mitigation: Review installed tools' destination and retention settings, and check quoted output for sensitive information before sharing.

## Reference(s):

- [Check on ClawHub](https://clawhub.ai/escoffier-labs/skills/check)
- [Publisher profile: escoffier-labs](https://clawhub.ai/user/escoffier-labs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with inline shell commands and quoted verification output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fresh verification after the last change and reports the actual command output and exit status.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
