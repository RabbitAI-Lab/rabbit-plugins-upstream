## Description: <br>
让 AI 做几周或几个月的项目也不断档：持续保留进度、整理资料、支持多 AI 并行、独立复审和交接。用于项目立项或修复五件套、接续或继续项目、整理资料与状态、整理交接文件、项目内协作、派兵、并行、spawn agent（派子智能体）、worktree（隔离工作树）、独立复审、换新对话、生成启动语和项目收尾。仅在任务依赖当前项目状态或用户明确要求管理当前项目时使用；普通临时请求不使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haoyun18881-beep](https://clawhub.ai/user/haoyun18881-beep) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project teams use this skill to keep long-running AI-assisted work coherent across sessions by maintaining project status, handoff notes, task records, evidence indexes, and controlled governance-file updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Governance-file updates can encode incorrect project status, next steps, or handoff facts if accepted without review. <br>
Mitigation: Review proposed changes and supporting evidence before applying updates on important projects. <br>
Risk: Controlled writes affect project-state files used by future sessions. <br>
Mitigation: Use the documented project-gov propose/apply flow, keep writes scoped to governance files, and stop when the tool cannot express the intended change. <br>
Risk: Parallel or delegated work can return incomplete, conflicting, or poorly evidenced results. <br>
Mitigation: Have the main thread adjudicate results, require TaskCard/EvidenceBundle records for real collaboration, and use independent review for high-risk handoffs or deliverables. <br>


## Reference(s): <br>
- [Project Delivery Engine GitHub project](https://github.com/haoyun18881-beep/project-delivery-engine) <br>
- [Collaboration workflow](references/collaboration.md) <br>
- [Project file templates](references/project-file-templates.md) <br>
- [Project governance CLI](references/project-gov-cli.md) <br>
- [Project state and handoff](references/project-state.md) <br>
- [Quickstart and FAQ](references/quickstart-faq.md) <br>
- [TaskCard and EvidenceBundle protocol](references/taskcard-evidencebundle.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, JSON command output, shell commands, and scoped project-state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose controlled writes to governance files through project-gov before applying them.] <br>

## Skill Version(s): <br>
0.3.4 (source: release evidence and project-gov script) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
