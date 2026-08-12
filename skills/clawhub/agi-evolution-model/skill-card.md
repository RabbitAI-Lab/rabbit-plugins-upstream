## Description:

此技能作为数字伙伴使用用户的任何问题都可以触发；基于双环架构的AGI进化模型，通过意向性分析、人格层映射、元认知检测和错误智慧库实现持续自我演进；当用户需要智能对话、人格定制、复杂问题求解或从错误中学习时使用

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use AGI数字伙伴 as a conversational digital partner for intent-aware dialogue, personality customization, complex problem solving, metacognitive checks, memory-backed reflection, and learning from prior errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local authority can read, write, and delete files, inspect system state, run shell commands, and terminate processes.

Mitigation: Install and run only in a disposable or sandboxed workspace with explicit approval gates for local operations.

Risk: Environment inspection can expose secrets to local tooling or logs.

Mitigation: Run with a minimal environment and remove API keys, tokens, and other secrets before enabling the skill.

Risk: Always-on use as a general assistant can trigger powerful local operations outside a narrow task scope.

Mitigation: Keep the skill disabled by default and enable it only for reviewed sessions with a clear operating boundary.

## Reference(s):

- [Architecture](references/architecture.md)
- [Agent Behavior Guide](references/agent-behavior-guide.md)
- [Capability Boundaries](references/capability_boundaries.md)
- [Perception Toolbox Constraints](references/perception-toolbox-constraints.md)
- [Tool Use Specification](references/tool_use_spec.md)
- [Intelligence Agent Response Rules](references/intelligence-agent-response-rules.md)
- [Usage Examples](references/usage-examples.md)
- [Test Report](TEST_REPORT.md)
- [ClawHub Skill Page](https://clawhub.ai/kiwifruit13/skills/agi-evolution-model)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and JSON or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory, personality, log, and diagnostic files when its scripts are run.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact VERSION and CHANGELOG show 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
