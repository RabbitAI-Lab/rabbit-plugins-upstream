## Description:

老孟中文编程（ZHC）智能体身份技能。当需要把 ZHC 语言服务接入编辑器或智能体运行时，或需要以智能体身份驱动 ZHC 的编译、运行、诊断、Office 导出闭环，或需要按分级门禁与冻结台账维护 ZHC 生态版本时使用本技能。适用于 LSP 接入、桥后端排障、产物降级判断、生态演进合规校验场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mxh678988](https://clawhub.ai/user/mxh678988)

### License/Terms of Use:

老孟中文编程许可条款

## Use Case:

Developers and automation agents use this skill to connect the ZHC language service to editors or agent runtimes, compile and diagnose ZHC programs, troubleshoot Office and web exports, and follow the documented compatibility and release workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security review marks the skill suspicious and reports incomplete scan coverage, with concerns about bridge descriptions, timeout handling, and build behavior.

Mitigation: Review bridge behavior and build handling before installation, confirm timeout settings, and limit host permissions and tools to those required by the workflow.

## Reference(s):

- [ZHC Agent workflow](references/智能体工作流.md)
- [LSP protocol and troubleshooting](references/LSP协议.md)
- [Bridge message protocol and fallback behavior](references/桥报文协议.md)
- [ZHC quick reference](references/快速参考.md)
- [ClawHub release page](https://clawhub.ai/mxh678988/skills/laomeng-zhc-agent)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [ZHC source code, shell commands, JSON diagnostics and bridge messages, and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compiled program and Office or web export files when the requested workflow produces them.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
