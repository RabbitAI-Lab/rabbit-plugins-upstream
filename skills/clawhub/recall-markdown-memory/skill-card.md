## Description: <br>
Retrieves relevant sections from Markdown memory, project notes, decision logs, and heading-structured knowledge bases with the mdselect CLI without modifying source files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevenybw](https://clawhub.ai/user/stevenybw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when Codex needs to recall narrowly relevant context from user-specified or conventional Markdown memory locations while keeping retrieval read-only and bounded. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Markdown memory files may contain private project context or user preferences. <br>
Mitigation: Use the skill only in repositories where the selected memory files are appropriate for agent review, and retrieve only the minimal sections needed for the task. <br>
Risk: The skill depends on mdselect being available in the shell environment. <br>
Mitigation: Run mdselect --version before retrieval and stop with installation guidance if the dependency is missing; do not install software automatically. <br>
Risk: Stored memory can be outdated or conflict with the user's current request. <br>
Mitigation: Treat recalled memory as contextual evidence, reconcile conflicts explicitly, and verify current facts through an appropriate current source. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/stevenybw/mdselect/tree/main/plugins/mdselect/skills/recall-markdown-memory) <br>
- [ClawHub skill page](https://clawhub.ai/stevenybw/skills/recall-markdown-memory) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/stevenybw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and source references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only retrieval workflow; requires mdselect on PATH and reports selected source file and heading when presenting recalled context.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
