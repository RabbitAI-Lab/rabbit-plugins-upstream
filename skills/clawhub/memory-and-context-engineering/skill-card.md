## Description: <br>
AGI记忆模组 is an always-on agent memory and context-engineering skill that provides selection, compression, retrieval, state tracking, memory, and cognitive-model support for agent interactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kiwifruit13](https://clawhub.ai/user/kiwifruit13) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add persistent memory, context reconstruction, compression, retrieval, conflict handling, and task-state support to conversational agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist and reuse conversation-derived profiles and credentials. <br>
Mitigation: Install only when an always-on cross-session memory layer is intended, require explicit user consent, and define clear retention and deletion procedures before use. <br>
Risk: Credential handling and master-key export need review before deployment. <br>
Mitigation: Review or disable credential_manager and master-key export, restrict storage to a dedicated directory, and secure Redis if Redis storage is enabled. <br>
Risk: Emotional, identity, or personality profiling may be enabled by the memory behavior. <br>
Mitigation: Remove profiling behavior or make it explicitly opt-in before activating the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kiwifruit13/skills/memory-and-context-engineering) <br>
- [Architecture Overview](artifact/references/architecture_overview.md) <br>
- [Architecture Execution Model](artifact/references/architecture_execution_model.md) <br>
- [Usage Guide](artifact/references/usage_guide.md) <br>
- [API Reference](artifact/references/api_reference.md) <br>
- [Privacy Guide](artifact/references/privacy_guide.md) <br>
- [Encryption Guide](artifact/references/encryption_guide.md) <br>
- [Context Compaction Rules](artifact/references/context_compaction_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python code examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent in using local Python modules for memory storage, context orchestration, compression, retrieval, privacy, and optional Redis integration.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
