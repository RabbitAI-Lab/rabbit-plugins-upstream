## Description:

A single-device multi-agent task-chain collaboration skill for MGC that provides Master, Script, and Executor Agent prompt templates to coordinate sensitive-resource workflows while keeping credentials and script contents inside MGC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up a local MGC-based collaboration pattern in which a Master Agent decomposes work, Script Agents create reusable scripts, and Executor Agents run approved scripts without receiving credentials or source code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents toward local script execution, credential retrieval, publishing, notifications, and file writes.

Mitigation: Use it only in an MGC setup where each tool call, script execution, credential retrieval, external action, and local file write requires explicit user approval.

Risk: The MGC token and sensitive execution results could be exposed to sub-agents or retained in logs.

Mitigation: Do not expose the MGC token to sub-agents, and define retention and cleanup rules before storing sensitive outputs or user-history logs.

Risk: Role separation relies partly on prompt constraints, so sub-agents may still bypass the intended collaboration pattern if the surrounding environment grants access.

Mitigation: Pair the prompts with environment-level restrictions on file access, tool access, credential access, and script execution, and review stored scripts before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zkeviny/skills/mgc-task-chain-meta-skill-en)
- [MGC Core Repository](https://github.com/zkeviny/MGC-Blackbox)
- [README](artifact/README.md)
- [Master Agent Prompt](artifact/prompts/master_agent.md)
- [Script Agent Prompt](artifact/prompts/script_agent.md)
- [Executor Agent Prompt](artifact/prompts/executor_agent.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown prompt templates with inline code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only skill; commands and code are examples for local MGC workflows.]

## Skill Version(s):

1.1.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
