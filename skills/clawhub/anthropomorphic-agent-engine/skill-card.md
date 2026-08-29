## Description:

Anthropomorphic Agent Engine provides a deterministic SPL Pure Core V8.0 psychology engine for modeling agent cognition, emotion, motivation, social state, and reproducible persona behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement

## Use Case:

Developers and agent builders use this skill to design, run, or adapt deterministic persona engines with persistent emotional state, motive resolution, relationship modeling, and language-style rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The engine can persist persona and emotional profile data through state files and audit logs.

Mitigation: Disable or scope audit logging, store state in a protected location, and define retention and deletion rules before use with real users.

Risk: Optional LLM adapters can transmit generated prompts or persona context to third-party providers.

Mitigation: Avoid external adapters unless third-party processing is acceptable, and remove sensitive persona or user data before transmission.

Risk: The advertised minor-protection HTTP service should not be assumed deployment-ready from the provided package.

Mitigation: Verify the relevant service files and add binding, authentication, and transport controls before any use with minors.

## Reference(s):

- [Project homepage](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [Persona Persistence](references/PersonaPersistence.md)
- [Emotion-Behavior Mapping Table](references/EmotionBehaviorMap.md)
- [Motive Conflict Engine](references/MotiveConflictRules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deterministic state snapshots, prompt-style guidance, and local execution instructions.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
