## Description:

Provides a configurable psychology engine for agent personas, including emotion, memory, trust, and age-gated minor-protection flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement v1.2 (dual-track)

## Use Case:

Developers use this skill to build stateful conversational personas, simulate emotional responses, and route younger users through a protected interaction flow. Commercial or organizational use requires separate authorization under the bundled license.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled minor-protection service has a serious guardian-token authorization flaw that could expose sensitive minor-safety data.

Mitigation: Keep the service bound to 127.0.0.1; do not expose it to a network until the guardian-token issue is fixed.

Risk: Stored logs and session records can contain sensitive minor-safety data.

Mitigation: Protect local files, disable unnecessary logging, and set a short retention period where appropriate.

Risk: Optional language-model adapters and guardian webhooks can transmit interaction data externally.

Mitigation: Enable networked integrations only with explicit user or guardian consent.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [Project homepage (declared in skill metadata)](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [Emotion-Behavior Mapping Table](references/EmotionBehaviorMap.md)
- [Persona Persistence](references/PersonaPersistence.md)
- [Motive Conflict Rules](references/MotiveConflictRules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Text or Markdown, with optional Python examples and state snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic core; optional language-model adapters produce networked, non-deterministic text.]

## Skill Version(s):

2.6.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
