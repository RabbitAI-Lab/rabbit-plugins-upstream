## Description:

Defines Daniel's default operating rules for agent execution, communication, reporting, and shared-skill rollout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daniel-refahi-ikara](https://clawhub.ai/user/daniel-refahi-ikara)

### License/Terms of Use:

MIT-0

## Use Case:

Daniel and administrators of Daniel-owned agents use this baseline to configure and audit persistent agent behavior across sessions, including direct execution, concise reporting, and verified shared-skill updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Direct-execution defaults may not match an agent's approval requirements.

Mitigation: Review the execution rules before rollout and retain human approval for sensitive or irreversible actions.

Risk: Persistent baseline rules can affect every session on an agent that loads them.

Mitigation: Apply only to intended Daniel-owned agents and test expected behavior after installation.

## Reference(s):

- [DR. Agent Baseline on ClawHub](https://clawhub.ai/daniel-refahi-ikara/skills/dr-agent-baseline)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown or plain text, with commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise completion receipts and one-step manual troubleshooting]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
