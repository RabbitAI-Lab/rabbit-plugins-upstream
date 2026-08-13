## Description:

Provides an always-on agent memory and context engineering layer for selection, compression, retrieval, state tracking, and cross-session memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and external agent builders use this skill to add persistent memory, context compression, retrieval, task-state tracking, and privacy-aware storage controls to agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on memory may retain identity, emotional, behavioral, and preference inferences across sessions.

Mitigation: Require explicit opt-in, define retention limits, and provide viewing, export, deletion, and consent-withdrawal controls before use.

Risk: Credential and key-management features increase exposure if secret storage is not intended.

Mitigation: Disable or isolate credential-management modules unless the deployment explicitly needs secret storage and has reviewed key-handling controls.

Risk: The security verdict requires review before deployment.

Mitigation: Review the release, run dependency and code scans, and confirm the privacy and security controls before enabling the skill in an agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/memory-and-context-engineering)
- [Architecture overview](references/architecture_overview.md)
- [API reference](references/api_reference.md)
- [Usage guide](references/usage_guide.md)
- [Privacy guide](references/privacy_guide.md)
- [Encryption guide](references/encryption_guide.md)
- [Security requirements](security-requirements.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code examples and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide agent behavior and may be paired with local memory, state, privacy, and credential-related files when the modules are used.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
