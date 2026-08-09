## Description: <br>
Create or refactor production-grade TypeScript agent applications. Use when the user asks Codex to generate, scaffold, restructure, or harden a TypeScript agent app, including CLI agents, web agent apps, API services, internal tools, multi-agent harnesses, workflow-first systems, model provider wiring, tool registries, memory/state stores, safety policies, and validation gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leogoat2004](https://clawhub.ai/user/leogoat2004) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to clarify requirements, select an agent-app architecture, generate or refactor TypeScript project files, and report real validation outcomes for production-grade agent application bases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated agent applications may involve package installs, file writes, network calls, credentials, databases, browser automation, or external API mutations. <br>
Mitigation: Review the proposed architecture and brief-to-file mapping before confirmation, and require approval gates for privileged or externally mutating actions. <br>
Risk: Missing credentials or unavailable live model access can lead to misleading validation claims. <br>
Mitigation: Report live LLM smoke tests as not run when credentials or approved network access are unavailable. <br>
Risk: A generated scaffold may be mistaken for a production-ready agent app if requirements, safety boundaries, and validation are skipped. <br>
Mitigation: Use the skill's decision gate, safety policy, and validation policy before implementing or accepting generated files. <br>


## Reference(s): <br>
- [Create Agent App README](README.md) <br>
- [Architecture Patterns](references/architecture-patterns.md) <br>
- [Generation Contract](references/generation-contract.md) <br>
- [Harness Contract](references/harness-contract.md) <br>
- [Provider Patterns](references/provider-patterns.md) <br>
- [Safety Policy](references/safety-policy.md) <br>
- [Validation Policy](references/validation-policy.md) <br>
- [Modern Selection Policy](references/modern-selection-policy.md) <br>
- [Official Docs](references/official-docs.md) <br>
- [Industry Architecture Signals](references/industry-architecture-signals.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/leogoat2004/skills/create-agent-app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown progress reports with generated TypeScript project files, configuration files, and validation command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an explicit user-confirmed architecture and validation plan before file generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
