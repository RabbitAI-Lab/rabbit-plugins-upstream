## Description:

Anthropomorphic psychology engine based on SPL Pure Core V8.0, enabling modular modeling of cognition, emotion, motivation, and social interaction. Supports fully reproducible continuous state personality simulation with zero probabilistic black boxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement

## Use Case:

Developers and agent builders use ai-soulmate to add deterministic personality state, emotion, motivation, relationship, and language-style rendering to anthropomorphic agents and character workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included chat server may be exposed without authentication if deployed on a network-facing host.

Mitigation: Bind it to localhost, add authentication and privacy controls before wider deployment, and review the service configuration before use.

Risk: Conversation logs, persona files, and audit JSONL records may contain sensitive user or state information.

Mitigation: Treat these files as sensitive records, disable or redirect logging where possible, protect storage locations, and delete old logs deliberately.

Risk: OpenAI or Anthropic adapters can send prompt content to external services when enabled.

Mitigation: Use external adapters only after explicit opt-in and consent, especially for minor-facing or mental-health-adjacent use cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [Project homepage](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [Persona Persistence](artifact/references/PersonaPersistence.md)
- [Emotion-Behavior Mapping Table](artifact/references/EmotionBehaviorMap.md)
- [Motive Conflict Engine](artifact/references/MotiveConflictRules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pure Python standard library modules; local JSONL audit logs may be created when engines run.]

## Skill Version(s):

2.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
