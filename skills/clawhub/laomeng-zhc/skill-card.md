## Description:

老孟中文编程（ZHC）技能帮助智能体编写、编译、运行和诊断中文语法的 ZHC 源码，并将表格数据导出为 CSV、XLSX、DOCX 或 HTML。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mxh678988](https://clawhub.ai/user/mxh678988)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and users of Chinese-language programming tools can use the skill to write or explain ZHC programs, diagnose compiler errors, and create table exports for office documents or web pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a build and execution weakness that may run a stale or substituted program; its analysis is incomplete.

Mitigation: Review the build and backend behavior, verify the program being run matches the intended source, and complete the security analysis before installation or execution.

## Reference(s):

- [ZHC-LANG-1.0 contract](references/契约_1.0.md)
- [Chinese quick reference](references/快速参考.md)
- [Chinese error code reference](references/错误码表_E_1.0.md)
- [ClawHub skill release](https://clawhub.ai/mxh678988/skills/laomeng-zhc)
- [Publisher profile](https://clawhub.ai/user/mxh678988)

## Skill Output:

**Output Type(s):** [Code, Text, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Chinese Markdown with .zc code blocks, command examples, diagnostic JSON, and generated program or export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [ZHC-LANG-1.0; Office export actions use OFFICE-WEB 2.4. Compilation requires Python and a C compiler; the documented Office bridge targets Windows x86-64.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
