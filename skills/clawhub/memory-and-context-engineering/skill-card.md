## Description:

AGI记忆模组 provides an always-on agent memory and context engineering layer for selection, compression, retrieval, state tracking, and cross-session memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent builders use this skill to add persistent memory and context management to agents. It supports context selection, compression, retrieval, state tracking, conflict handling, and cross-session memory when explicit consent and storage controls are in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run as an always-on memory layer and persist interaction history or inferred user traits across sessions.

Mitigation: Require explicit user consent, document retention settings, and disable categories such as emotional or psychometric profiling unless they are required.

Risk: Broad local and Redis-backed storage can retain sensitive user data longer than intended.

Mitigation: Use a dedicated storage directory and Redis endpoint with strict permissions, retention limits, encryption, and deletion/export controls.

Risk: Credential management and unsafe key or temporary-file handling may expose secrets.

Mitigation: Remove or isolate credential handling, replace unsafe key and temporary-file flows, and review secrets handling before deployment.

Risk: Hard-coded external health checks or network behavior can create unexpected outbound connections.

Mitigation: Block the external health check by default and require an explicit egress review before enabling network access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/memory-and-context-engineering)
- [Architecture overview](references/architecture_overview.md)
- [Dual-track architecture overview](references/dual_track_architecture_overview.md)
- [Usage guide](references/usage_guide.md)
- [Privacy guide](references/privacy_guide.md)
- [Encryption guide](references/encryption_guide.md)
- [API reference](references/api_reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, Python code snippets, shell commands, and structured memory or context records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include retrieved context, compressed summaries, memory records, configuration guidance, and integration code.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
