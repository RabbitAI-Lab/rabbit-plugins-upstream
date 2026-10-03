## Description:

Models a conversational agent's emotional and social state with a deterministic local psychology engine and optional text-generation adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement

## Use Case:

Developers use the skill to build agents with persistent, evolving personality states, inspect state changes, and adapt conversational behavior. Commercial or organizational use requires prior written paid authorization under the bundled license.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit and request logs may retain sensitive emotional-state information by default.

Mitigation: Set SPL_AUDIT_LOG=0 and SPL_LOG=0 for silent mode; otherwise restrict log access and define retention and deletion practices.

Risk: Changing the demo server bind address can expose its chat endpoint beyond the local machine.

Mitigation: Keep the default loopback bind; do not set SPL_BIND=0.0.0.0 without access controls and network-exposure review.

Risk: Opt-in OpenAI or Claude adapters can send input-derived prompts outside the machine.

Mitigation: Leave adapters disabled unless users explicitly consent to the data transfer.

Risk: ClawHub's MIT-0 license label conflicts with the bundled dual-track license, which restricts organizational and commercial use.

Mitigation: Confirm governing license terms with the publisher and obtain written paid authorization before organizational or commercial deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [Project homepage (ClawHub metadata; source provenance unavailable)](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [Persona persistence contract](references/PersonaPersistence.md)
- [Emotion-behavior mapping](references/EmotionBehaviorMap.md)
- [Motive conflict rules](references/MotiveConflictRules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown with Python examples and structured state guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-core replay requires an injected virtual clock; optional LLM-generated text is not deterministic.]

## Skill Version(s):

2.5.2 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
