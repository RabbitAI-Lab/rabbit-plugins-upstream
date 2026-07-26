## Description: <br>
AI编码异常处理控制框架在编码、需求分析、设计、测试、代码审查和重构任务中引导代理使用调研、需求设计、异常场景穷举、测试、审查和复盘闭环来减少仅覆盖 happy path 的实现。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[llimage](https://clawhub.ai/user/llimage) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to structure AI-assisted software work around explicit failure modes, exception handling, test coverage, review handoff, and lessons learned. It is most useful for coding workflows where reliability, security checks, and repeatable review gates matter more than speed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate broadly for normal coding, design, testing, review, and refactoring requests. <br>
Mitigation: Use a narrow explicit activation phrase and confirm that the user wants this heavier governance workflow before applying it to routine tasks. <br>
Risk: The workflow directs agents to use WebSearch/WebFetch and perform project file writes. <br>
Mitigation: Require user confirmation before network research or filesystem writes, and keep source URLs and dates in generated research artifacts. <br>
Risk: Persistent `.workbuddy` memory and audit-ledger files may be created in sensitive repositories. <br>
Mitigation: Enable project memory only in repositories where this is intended, and exclude secrets, credentials, internal paths, and confidential review notes from shared outputs. <br>
Risk: Chaos-test guidance can be disruptive if executed against production or shared services. <br>
Mitigation: Replace chaos examples with local or staging-only placeholders and enforce explicit environment guards before any fault-injection command is run. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/llimage/skills/ai-coding-exception-control) <br>
- [Publisher Profile](https://clawhub.ai/user/llimage) <br>
- [README.md](README.md) <br>
- [Requirements and Design SOP](references/requirements-design-sop.md) <br>
- [Coding SOP](references/coding-sop.md) <br>
- [Testing SOP](references/testing-sop.md) <br>
- [Lessons Feedback Loop](references/lessons-feedback-loop.md) <br>
- [Audit-Ledger Specification](references/audit-ledger-spec.md) <br>
- [Template Collection](references/templates.md) <br>
- [OPC Development Suite](references/OPC-DEVELOPMENT-SUITE.md) <br>
- [Reverse Requirements Example](references/reverse-requirements.md) <br>
- [Reverse Design Example](references/reverse-design.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with checklists, templates, code examples, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the agent to create or update project memory, review ledger files, tests, and implementation artifacts when activated.] <br>

## Skill Version(s): <br>
1.7.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
