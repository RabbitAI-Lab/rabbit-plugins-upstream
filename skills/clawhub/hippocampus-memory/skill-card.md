## Description: <br>
Persistent memory system for AI agents with automatic encoding, decay, and semantic reinforcement, based on Stanford Generative Agents (Park et al., 2023). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[impkind](https://clawhub.ai/user/impkind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external OpenClaw users use this skill to give agents persistent local memory, including conversation signal extraction, importance scoring, recall, decay, and generated core-memory context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process broad OpenClaw conversation history into durable local memory files. <br>
Mitigation: Install only when persistent local memory is intended; keep the default limited first run or use --signals N instead of --whole unless historical backfill is acceptable. <br>
Risk: Memory files such as memory/index.json and HIPPOCAMPUS_CORE.md may contain sensitive personal context. <br>
Mitigation: Add generated memory files to .gitignore and periodically inspect or delete stored memory files. <br>
Risk: Optional cron jobs can repeatedly encode recent conversations without active per-run review. <br>
Mitigation: Review or disable the cron setup before running install.sh --with-cron and keep encoding scoped to expected workspaces and agents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/impkind/skills/hippocampus-memory) <br>
- [Project repository declared in OpenClaw metadata](https://github.com/ImpKind/hippocampus-skill) <br>
- [Stanford Generative Agents paper](https://arxiv.org/abs/2304.03442) <br>
- [Generative Agents reference implementation](https://github.com/joonspk-research/generative_agents) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and local JSON/Markdown memory files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local memory/index.json, pending memory JSON, and HIPPOCAMPUS_CORE.md when installed and run.] <br>

## Skill Version(s): <br>
3.8.6 (source: server release metadata, OpenClaw metadata, CHANGELOG, released 2026-02-05) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
