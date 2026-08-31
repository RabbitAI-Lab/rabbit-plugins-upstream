## Description:

ai-soulmate is a deterministic SPL Pure Core V8.0 anthropomorphic psychology engine that models cognition, emotion, motivation, and social state for reproducible persona simulations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

Software License Agreement Version 1.1

## Use Case:

Developers and agent builders use this skill to add deterministic persona-state modeling, emotional behavior mapping, motive-conflict handling, language-style rendering, and minor-protection workflows to long-running agents or character simulations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The minor-focused HTTP service is unauthenticated and binds to all interfaces by default.

Mitigation: Run the service only on a trusted machine or network, bind it to localhost, and add authentication before any exposed use.

Risk: Raw JSONL logging may store sensitive conversations, including minor-focused interactions.

Mitigation: Disable or minimize raw logging unless users and guardians understand what is stored, and protect any retained logs.

Risk: Optional OpenAI or Anthropic adapter paths may send interaction data to remote services.

Mitigation: Enable remote-processing adapters only with explicit consent and clear data-handling expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [Project homepage](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [PersonaPersistence.md](references/PersonaPersistence.md)
- [EmotionBehaviorMap.md](references/EmotionBehaviorMap.md)
- [MotiveConflictRules.md](references/MotiveConflictRules.md)
- [spl-agent-engine on PyPI](https://pypi.org/project/spl-agent-engine/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell snippets; runtime modules can emit JSON snapshots and JSONL audit logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python standard-library modules and optional local HTTP service behavior.]

## Skill Version(s):

2.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
