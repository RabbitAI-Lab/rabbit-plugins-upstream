## Description: <br>
通过自然语言指令驱动浏览器交互的命令行工具，支持导航、动作执行、结构化数据提取、元素观察、截图和关闭浏览器。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to drive browser workflows with natural language commands for web navigation, form interaction, screenshots, element observation, and structured extraction. It is suited to deliberate browser automation and prototype validation where local Chrome or an optional remote browser service is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live browser automation can click, submit forms, or extract page data in ways the user did not intend. <br>
Mitigation: Use only for deliberate browser-automation tasks, review each target workflow before execution, and verify results with screenshots or observe commands. <br>
Risk: Remote browser mode may run sessions through Browserbase when API keys are configured. <br>
Mitigation: Treat Browserbase credentials as sensitive, avoid entering secrets into automated sessions, and use remote mode only when its data path is acceptable. <br>
Risk: The security verdict flags under-disclosed activation scope and live/remote browser behavior. <br>
Mitigation: Review the skill before installation and restrict use to accounts and pages where unintended interactions would not cause material impact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-automation-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser command sequences, screenshots guidance, structured extraction schemas, execution logs, and error-handling guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
