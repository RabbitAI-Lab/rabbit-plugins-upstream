## Description: <br>
HeartFlow is a local JavaScript cognitive engine that produces structured cognitive state for AI agent pipelines across memory, emotion, reasoning, code execution, search, and self-evolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use HeartFlow as a local cognitive preprocessing layer that converts user input into structured emotion, psychology, philosophy, desire, judgment, memory, and decision-routing signals for downstream agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory and state can retain sensitive user or project information. <br>
Mitigation: Install only when a persistent local cognitive and memory engine is desired, and review or configure the data directories it creates. <br>
Risk: MCP exposure can create unauthorized access risk if the listener is reachable without appropriate controls. <br>
Mitigation: Set HEARTFLOW_MCP_TOKEN before exposing MCP and keep the MCP listener bound to localhost unless a controlled deployment requires otherwise. <br>
Risk: Code execution and self-modification features can execute untrusted logic when explicitly enabled. <br>
Mitigation: Enable HEARTFLOW_CODE_EXECUTOR_ENABLED or self-modification flags only for trusted code in controlled projects. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yun520-1/skills/heartflow) <br>
- [README](artifact/README.md) <br>
- [Installation Guide](artifact/INSTALL.md) <br>
- [Research Paper Index](artifact/src/research/paper-index.js) <br>
- [Benchmark Report v5.5.1](artifact/docs/benchmark-report-v5.5.1.md) <br>
- [Audit Report v5.3.0](artifact/docs/audit-report-v5.3.0.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Structured text and JSON-like cognitive state, with CLI/MCP commands and JavaScript integration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact states that HeartFlow produces structured cognitive state rather than conversation, and code execution, network access, file writes, and credential access require explicit user configuration.] <br>

## Skill Version(s): <br>
5.7.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
